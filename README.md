<p align="center">
  <a href="https://github.com/OpenSelena">
    <img src="assets/logo.png" alt="OpenSelena Logo" width="100" height="100" />
  </a>
</p>

<h1 align="center">OpenSelena Homebrew Tap</h1>

<p align="center">
  Official Homebrew tap for <a href="https://github.com/OpenSelena/libreget">LibreGet</a>, <a href="https://github.com/OpenSelena/open-omni">Open Omni</a>, and <a href="https://github.com/OpenSelena/open-nami">Open Nami</a>.<br />
  Follows standard Homebrew tap layout (<code>Formula/</code>, <code>Casks/</code>, <code>cask_renames.json</code>) with automated upstream release sync.
</p>

<p align="center">
  <a href="https://github.com/OpenSelena/homebrew-tap/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/OpenSelena/homebrew-tap/tests.yml?style=for-the-badge&label=audit&logo=githubactions&logoColor=white" alt="Tap Audit Status" /></a>
  <a href="https://github.com/OpenSelena/homebrew-tap/actions/workflows/sync.yml"><img src="https://img.shields.io/github/actions/workflow/status/OpenSelena/homebrew-tap/sync.yml?style=for-the-badge&label=auto-sync&logo=homebrew&logoColor=white" alt="Tap Sync Status" /></a>
  <a href="https://github.com/OpenSelena/libreget/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/libreget?style=for-the-badge&label=LibreGet&color=F28500" alt="LibreGet Release" /></a>
  <a href="https://github.com/OpenSelena/open-omni/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/open-omni?style=for-the-badge&label=Open%20Omni&color=10b981" alt="Open Omni Release" /></a>
  <a href="https://github.com/OpenSelena/open-nami/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/open-nami?style=for-the-badge&label=Open%20Nami&color=C15F3C" alt="Open Nami Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2AA845?style=for-the-badge" alt="License MIT" /></a>
</p>

---

## Packages

| Package | Type | Platforms | Description |
| :--- | :--- | :--- | :--- |
| <img src="https://api.iconify.design/ph/desktop.svg?color=%23F28500" width="18" height="18" align="absmiddle" alt="LibreGet" />&nbsp;[LibreGet](https://github.com/OpenSelena/libreget) | Cask | macOS | Desktop media downloader and tool hub |
| <img src="https://api.iconify.design/ph/terminal-window.svg?color=%2310B981" width="18" height="18" align="absmiddle" alt="Open Omni" />&nbsp;[Open&nbsp;Omni](https://github.com/OpenSelena/open-omni) | Formula | macOS,&nbsp;Linux | Terminal media downloader & TUI for 1,800+ sites |
| <img src="https://api.iconify.design/ph/images.svg?color=%23C15F3C" width="18" height="18" align="absmiddle" alt="Open Nami" />&nbsp;[Open&nbsp;Nami](https://github.com/OpenSelena/open-nami) | Formula | macOS,&nbsp;Linux | Bulk downloader for Instagram, TikTok, Facebook & X |

---

## <img src="https://api.iconify.design/ph/download-simple.svg?color=%231E6FE8" width="22" height="22" align="absmiddle" alt="Install" />&nbsp;How do I install these packages?

### Direct install (recommended)

```sh
# Formulae (macOS & Linux)
brew install OpenSelena/tap/open-omni
brew install OpenSelena/tap/open-nami

# Cask (macOS)
brew install --cask OpenSelena/tap/libreget
```

### Tap first

```sh
brew tap OpenSelena/tap
brew install open-omni open-nami
brew install --cask libreget
```

### `Brewfile` (`brew bundle`)

```ruby
tap "OpenSelena/tap"
brew "open-omni"
brew "open-nami"
cask "libreget"
```

### <img src="https://api.iconify.design/ph/shield-check.svg?color=%232AA845" width="18" height="18" align="absmiddle" alt="Trust" />&nbsp;Trusting a third-party tap

Recent Homebrew releases require explicit trust for non-official taps. If Homebrew prompts or refuses to load a third-party package, trust the tap or individual formula/cask:

```sh
# Trust the whole tap
brew trust --tap OpenSelena/tap

# Or trust a single formula / cask
brew trust --formula OpenSelena/tap/open-nami
brew trust --cask OpenSelena/tap/libreget
```

---

## <img src="https://api.iconify.design/ph/package.svg?color=%23F28500" width="22" height="22" align="absmiddle" alt="Manage" />&nbsp;Upgrade and uninstall

```sh
# Upgrade everything from this tap
brew update
brew upgrade open-omni open-nami
brew upgrade --cask libreget

# Uninstall packages
brew uninstall open-omni open-nami
brew uninstall --cask libreget

# Remove the tap
brew untap OpenSelena/tap
```

Legacy `omniget` cask installs migrate to `libreget` via [cask_renames.json](cask_renames.json).

---

## <img src="https://api.iconify.design/ph/arrows-clockwise.svg?color=%232AA845" width="22" height="22" align="absmiddle" alt="Sync" />&nbsp;Automated sync and validation

- **[Sync Upstream Packages](.github/workflows/sync.yml)**: Polls npm (`open-nami`) and GitHub Releases (`OpenSelena/open-omni`, `OpenSelena/libreget`) every 15 minutes (`schedule`), on manual `workflow_dispatch`, or on `repository_dispatch` (`release-published`), recomputing SHA-256 checksums via [sync_tap.py](scripts/sync_tap.py).
- **[Tap Audit & Validation](.github/workflows/tests.yml)**: Runs `ruby -c` and verifies every download URL and SHA-256 digest on pushes and pull requests.

---

## <img src="https://api.iconify.design/ph/wrench.svg?color=%236F6F75" width="22" height="22" align="absmiddle" alt="Troubleshooting" />&nbsp;Troubleshooting

If `brew update` fails or serves stale manifests:

```sh
brew update-reset && brew update
brew doctor
```

Report packaging bugs in the [homebrew-tap issue tracker](https://github.com/OpenSelena/homebrew-tap/issues).

---

## <img src="https://api.iconify.design/ph/book-open.svg?color=%23C15F3C" width="22" height="22" align="absmiddle" alt="Documentation" />&nbsp;Documentation and license

`brew help`, `man brew`, or check [Homebrew's documentation](https://docs.brew.sh).

- **[LibreGet](https://github.com/OpenSelena/libreget)** — Desktop app & tool hub ([companion extension](https://github.com/OpenSelena/libreget-extension))
- **[Open Omni](https://github.com/OpenSelena/open-omni)** — Terminal downloader & TUI
- **[Open Nami](https://github.com/OpenSelena/open-nami)** — Profile archiver CLI & TUI

[MIT](LICENSE) — maintained by [OpenSelena](https://github.com/OpenSelena).
