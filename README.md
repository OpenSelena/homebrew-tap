<p align="center">
  <a href="https://github.com/OpenSelena">
    <img src="assets/logo.png" alt="OpenSelena Logo" width="100" height="100" />
  </a>
</p>

<h1 align="center">OpenSelena Homebrew Tap</h1>

<p align="center">
  Official Homebrew tap for <a href="https://github.com/OpenSelena/libreget">LibreGet</a>, <a href="https://github.com/OpenSelena/open-omni">Open Omni</a>, and <a href="https://github.com/OpenSelena/open-nami">Open Nami</a>.<br>
  Formulas and casks sync automatically every 15 minutes from upstream npm and GitHub releases.
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

| Package | Type | Target | Install command |
| :--- | :--- | :--- | :--- |
| <img src="https://api.iconify.design/ph/desktop.svg?color=%23F28500" width="18" height="18" align="center" alt="Desktop" /> **[LibreGet](https://github.com/OpenSelena/libreget)** | Cask | macOS *(Apple Silicon & Intel)* | `brew install --cask OpenSelena/tap/libreget` |
| <img src="https://api.iconify.design/ph/terminal-window.svg?color=%2310B981" width="18" height="18" align="center" alt="CLI" /> **[Open Omni](https://github.com/OpenSelena/open-omni)** | Formula | macOS & Linux | `brew install OpenSelena/tap/open-omni` |
| <img src="https://api.iconify.design/ph/images.svg?color=%23C15F3C" width="18" height="18" align="center" alt="Profiles" /> **[Open Nami](https://github.com/OpenSelena/open-nami)** | Formula | macOS & Linux | `brew install OpenSelena/tap/open-nami` |

*(Legacy `omniget` cask installs automatically migrate to `libreget` via `cask_renames.json`.)*

---

## Install & Upgrade

```sh
# Add the tap once (optional if using OpenSelena/tap/<pkg> directly)
brew tap OpenSelena/tap

# Install
brew install --cask libreget
brew install open-omni open-nami

# Upgrade to latest synced versions
brew update && brew upgrade open-omni open-nami && brew upgrade --cask libreget
```

---

## Real-Time Sync & Validation

- [Sync workflow](.github/workflows/sync.yml) polls upstream npm (`open-nami`) and GitHub Releases (`OpenSelena/open-omni`, `OpenSelena/libreget`) every 15 minutes (`schedule`), on manual `workflow_dispatch`, or on `repository_dispatch` (`release-published`), recomputing and verifying SHA-256 digests via [sync_tap.py](scripts/sync_tap.py).
- [Tap Audit & Validation](.github/workflows/tests.yml) checks Ruby syntax and verifies every download URL and SHA-256 checksum on pushes and pull requests.

---

## License

[MIT](LICENSE) — maintained by [OpenSelena](https://github.com/OpenSelena).
