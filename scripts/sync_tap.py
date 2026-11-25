#!/usr/bin/env python3
"""Synchronize and verify OpenSelena Homebrew formulas and casks against upstream releases."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

TARGETS: list[dict[str, str]] = [
    {
        "name": "open-nami",
        "kind": "npm",
        "path": "Formula/open-nami.rb",
        "package": "open-nami",
    },
    {
        "name": "open-omni",
        "kind": "github_formula",
        "path": "Formula/open-omni.rb",
        "repo": "OpenSelena/open-omni",
        "asset_suffix": ".tgz",
    },
    {
        "name": "libreget",
        "kind": "github_cask",
        "path": "Casks/libreget.rb",
        "repo": "OpenSelena/libreget",
        "arm_suffix": "aarch64.dmg",
        "intel_suffix": "x64.dmg",
    },
]


def http_get_bytes(url: str, accept: str | None = None) -> bytes:
    """Fetch a remote URL with optional GitHub Actions token authentication."""
    headers = {"User-Agent": "OpenSelena-Homebrew-Tap/1.0"}
    if accept:
        headers["Accept"] = accept
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        return resp.read()


def http_get_json(url: str) -> dict[str, Any]:
    """Fetch and parse a JSON endpoint."""
    raw = http_get_bytes(url, accept="application/vnd.github+json")
    return json.loads(raw.decode("utf-8"))


def fetch_github_latest_release(repo: str) -> dict[str, Any]:
    """Fetch latest GitHub release tag and assets, falling back when REST API is rate-limited."""
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    if os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"):
        try:
            return http_get_json(api_url)
        except urllib.error.HTTPError as exc:
            if exc.code not in (403, 429):
                raise

    req = urllib.request.Request(
        f"https://github.com/{repo}/releases/latest",
        headers={"User-Agent": "OpenSelena-Homebrew-Tap/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        final_url = resp.geturl()

    if "/releases/tag/" not in final_url:
        raise RuntimeError(f"Unexpected latest release redirect URL for {repo}: {final_url}")

    tag = urllib.parse.unquote(final_url.rsplit("/releases/tag/", 1)[1].split("?")[0])
    expanded_url = final_url.replace("/releases/tag/", "/releases/expanded_assets/")
    html = http_get_bytes(expanded_url).decode("utf-8", errors="replace")

    rel_paths = re.findall(r'href="(/[^"]+/releases/download/[^"]+)"', html)
    assets = [
        {
            "name": urllib.parse.unquote(rel.rsplit("/", 1)[1]),
            "browser_download_url": f"https://github.com{rel}",
        }
        for rel in rel_paths
    ]
    return {"tag_name": tag, "assets": assets}


def sha256_url(url: str) -> str:
    """Download an archive and return its lowercase SHA-256 hex digest."""
    req = urllib.request.Request(url, headers={"User-Agent": "Homebrew/4.0"})
    digest = hashlib.sha256()
    with urllib.request.urlopen(req, timeout=120) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        while chunk := resp.read(65536):
            digest.update(chunk)
    return digest.hexdigest()


def replace_first(pattern: str, repl: str, text: str, label: str) -> str:
    """Replace the first regex match or raise when a required manifest field is missing."""
    updated, count = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise ValueError(f"Expected 1 match for {label}, found {count}")
    return updated


def replace_arch_block(text: str, arch: str, sha: str, url: str) -> str:
    """Update sha256 and url inside an on_arm or on_intel block preserving stanza order."""
    pattern = rf'(on_{arch} do\s*\n\s*sha256 ")([a-fA-F0-9]{{64}})("\s*\n\s*\n\s*url ")([^"]+)(")'
    match = re.search(pattern, text)
    if not match:
        raise ValueError(f"Could not locate on_{arch} block in cask")
    return (
        text[: match.start()]
        + f"{match.group(1)}{sha}{match.group(3)}{url}{match.group(5)}"
        + text[match.end() :]
    )


def template_cask_url(url: str, tag: str, version: str) -> str:
    """Replace concrete release tag/version segments with Homebrew #{version} placeholders."""
    templated = url
    if tag == f"v{version}":
        templated = templated.replace(f"/v{version}/", "/v#{version}/")
    elif tag == version:
        templated = templated.replace(f"/{version}/", "/#{version}/")
    filename_prefix, sep, filename = templated.rpartition("/")
    filename = filename.replace(version, "#{version}")
    return f"{filename_prefix}{sep}{filename}"


def find_asset_url(assets: list[dict[str, Any]], suffix: str) -> str | None:
    """Return browser_download_url for the first asset matching a lowercase suffix."""
    lower_suffix = suffix.lower()
    for asset in assets:
        name = str(asset.get("name", ""))
        if name.lower().endswith(lower_suffix):
            return str(asset["browser_download_url"])
    return None


def sync_formula(target: dict[str, str], force: bool = False) -> bool:
    """Sync a npm or GitHub tarball formula. Returns True if file contents changed."""
    fpath = ROOT / target["path"]
    content = fpath.read_text(encoding="utf-8")

    if target["kind"] == "npm":
        data = http_get_json(f"https://registry.npmjs.org/{target['package']}/latest")
        next_url = str(data["dist"]["tarball"])
    else:
        release = fetch_github_latest_release(target["repo"])
        next_url = find_asset_url(release.get("assets", []), target["asset_suffix"])
        if not next_url:
            print(f"[SKIP] {target['name']}: no {target['asset_suffix']} asset on latest release")
            return False

    cur_url_match = re.search(r'^\s*url "([^"]+)"', content, flags=re.MULTILINE)
    if not cur_url_match:
        raise ValueError(f"Missing url in {target['path']}")
    cur_url = cur_url_match.group(1)

    if cur_url == next_url and not force:
        print(f"[OK] {target['name']}: already at {cur_url}")
        return False

    next_sha = sha256_url(next_url)
    updated = replace_first(r'^(\s*url )"[^"]+"', rf'\1"{next_url}"', content, f"{target['name']} url")
    updated = replace_first(
        r'^(\s*sha256 )"[a-fA-F0-9]{64}"',
        rf'\1"{next_sha}"',
        updated,
        f"{target['name']} sha256",
    )

    if updated == content:
        print(f"[OK] {target['name']}: unchanged")
        return False

    fpath.write_text(updated, encoding="utf-8")
    print(f"[UPDATED] {target['name']} -> {next_url} ({next_sha})")
    return True


def sync_cask(target: dict[str, str], force: bool = False) -> bool:
    """Sync an arm64 + x64 DMG cask from GitHub Releases. Returns True if changed."""
    fpath = ROOT / target["path"]
    content = fpath.read_text(encoding="utf-8")

    release = fetch_github_latest_release(target["repo"])
    tag = str(release["tag_name"])
    version = tag.removeprefix("v")
    assets = release.get("assets", [])

    arm_url = find_asset_url(assets, target["arm_suffix"])
    intel_url = find_asset_url(assets, target["intel_suffix"])
    if not arm_url or not intel_url:
        print(f"[SKIP] {target['name']}: release {tag} missing arm or intel DMG asset")
        return False

    arm_tpl = template_cask_url(arm_url, tag, version)
    intel_tpl = template_cask_url(intel_url, tag, version)

    cur_ver_match = re.search(r'^\s*version "([^"]+)"', content, flags=re.MULTILINE)
    cur_ver = cur_ver_match.group(1) if cur_ver_match else ""
    if cur_ver == version and arm_tpl in content and intel_tpl in content and not force:
        print(f"[OK] {target['name']}: already at {version}")
        return False

    arm_sha = sha256_url(arm_url)
    intel_sha = sha256_url(intel_url)

    updated = replace_first(
        r'^(\s*version )"[^"]+"',
        rf'\1"{version}"',
        content,
        f"{target['name']} version",
    )
    updated = replace_arch_block(updated, "arm", arm_sha, arm_tpl)
    updated = replace_arch_block(updated, "intel", intel_sha, intel_tpl)

    if updated == content:
        print(f"[OK] {target['name']}: unchanged")
        return False

    fpath.write_text(updated, encoding="utf-8")
    print(f"[UPDATED] {target['name']} -> {version}")
    return True


def verify_tap() -> int:
    """Verify all formula/cask download URLs, SHA-256 digests, and cask_renames.json."""
    failed = False
    manifests = sorted(
        list((ROOT / "Formula").glob("*.rb")) + list((ROOT / "Casks").glob("*.rb"))
    )

    for path in manifests:
        content = path.read_text(encoding="utf-8")
        ver_match = re.search(r'version ["\']([^"\']+)["\']', content)
        version = ver_match.group(1) if ver_match else ""

        urls = re.findall(r'url ["\']([^"\']+)["\']', content)
        shas = re.findall(r'sha256 ["\']([a-fA-F0-9]{64})["\']', content)
        rel = path.relative_to(ROOT)

        if len(urls) != len(shas):
            print(f"[FAIL] {rel}: url count ({len(urls)}) != sha256 count ({len(shas)})")
            failed = True
            continue

        for raw_url, expected_sha in zip(urls, shas):
            resolved = raw_url.replace("#{version}", version)
            print(f"Checking {rel} -> {resolved}")
            try:
                actual_sha = sha256_url(resolved)
                if actual_sha.lower() != expected_sha.lower():
                    print(f"  [FAIL] SHA256 mismatch: expected {expected_sha}, got {actual_sha}")
                    failed = True
                else:
                    print("  [PASS] SHA256 matches.")
            except (urllib.error.URLError, RuntimeError, OSError) as exc:
                print(f"  [FAIL] {exc}")
                failed = True

    renames_path = ROOT / "cask_renames.json"
    if renames_path.exists():
        try:
            renames = json.loads(renames_path.read_text(encoding="utf-8"))
            if not isinstance(renames, dict):
                raise ValueError("cask_renames.json must map old -> new names")
            for old_name, new_name in renames.items():
                if not (ROOT / "Casks" / f"{new_name}.rb").exists():
                    raise FileNotFoundError(
                        f"cask_renames.json target Casks/{new_name}.rb missing for {old_name}"
                    )
            print(f"Checked cask_renames.json -> {len(renames)} mapping(s) valid.")
        except Exception as exc:
            print(f"[FAIL] cask_renames.json: {exc}")
            failed = True

    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync and verify OpenSelena Homebrew tap.")
    parser.add_argument("--sync", action="store_true", help="Update manifests from upstream releases")
    parser.add_argument("--verify", action="store_true", help="Verify all URLs and SHA-256 digests")
    parser.add_argument("--package", default="all", help="Package name filter for --sync (default: all)")
    parser.add_argument("--force", action="store_true", help="Recompute checksums even if URL matches")
    args = parser.parse_args()

    if not args.sync and not args.verify:
        parser.error("Specify --sync and/or --verify")

    selected = TARGETS if args.package == "all" else [t for t in TARGETS if t["name"] == args.package]
    if args.sync and not selected:
        valid = ", ".join(t["name"] for t in TARGETS)
        print(f"Unknown package '{args.package}'. Expected 'all' or one of: {valid}", file=sys.stderr)
        return 1

    if args.sync:
        changed = False
        for target in selected:
            if target["kind"] == "github_cask":
                changed = sync_cask(target, force=args.force) or changed
            else:
                changed = sync_formula(target, force=args.force) or changed
        print(f"Sync complete (changed={changed}).")

    if args.verify:
        rc = verify_tap()
        if rc != 0:
            return rc

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
