<p align="center">
  <img src="assets/logo.png" alt="OpenSelena" width="160" />
</p>

<h1 align="center">OpenSelena Homebrew Tap</h1>

<p align="center">
  Official <a href="https://brew.sh/">Homebrew</a> tap for <a href="https://github.com/OpenSelena">OpenSelena</a> projects.
</p>

<p align="center">
  <a href="https://brew.sh/"><img src="https://img.shields.io/badge/Homebrew-Tap-FBB040.svg?logo=homebrew&logoColor=white" alt="Homebrew Tap" /></a>
  <a href="https://github.com/OpenSelena/homebrew-tap"><img src="https://img.shields.io/badge/packages-3-brightgreen.svg" alt="Packages" /></a>
  <a href="https://github.com/OpenSelena/homebrew-tap"><img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg?logo=apple&logoColor=white" alt="Platform" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
</p>

---

## Install

```sh
brew install OpenSelena/tap/<formula>
```

Or add the tap first, then install by name:

```sh
brew tap OpenSelena/tap
brew install <formula>
```

## Available Packages

### Formulae

| Formula | Description |
| :--- | :--- |
| `open-omni` | Terminal media downloader & TUI for 1,800+ sites |
| `open-nami` | Bulk social media downloader for Instagram, TikTok, Facebook & X |

```sh
brew install OpenSelena/tap/open-omni
brew install OpenSelena/tap/open-nami
```

### Casks

| Cask | Description |
| :--- | :--- |
| `omniget` | Universal desktop media workstation (macOS) |

```sh
brew install --cask OpenSelena/tap/omniget
```

## Documentation & Issues

Each project has its own repository with full documentation:

- [openomni](https://github.com/OpenSelena/openomni) — open-omni CLI
- [open-nami](https://github.com/OpenSelena/open-nami) — open-nami CLI
- [omniget](https://github.com/OpenSelena/omniget) — OmniGet desktop app

For tap-specific packaging issues, use the [homebrew-tap issue tracker](https://github.com/OpenSelena/homebrew-tap/issues).

## License

[MIT](LICENSE)
