<p align="center">
  <a href="https://github.com/OpenSelena/libreget">
    <img src="assets/logo.png" alt="OpenSelena Logo" width="100" height="100" />
  </a>
</p>

<h1 align="center">OpenSelena Homebrew Tap</h1>

<p align="center">
  Official Homebrew distribution channel for <a href="https://github.com/OpenSelena/libreget">LibreGet</a> and OpenSelena media tools.<br>
  Install and update desktop applications and CLI tools on macOS and Linux with one command.
</p>

<p align="center">
  <a href="https://brew.sh/"><img src="https://img.shields.io/badge/Homebrew-Tap-FBB040?style=for-the-badge&logo=homebrew&logoColor=white" alt="Homebrew" /></a>
  <a href="https://github.com/OpenSelena/libreget/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/libreget?style=for-the-badge&label=LibreGet&color=F28500" alt="LibreGet Release" /></a>
  <a href="https://github.com/OpenSelena/openomni/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/openomni?style=for-the-badge&label=Open%20Omni&color=10b981" alt="Open Omni" /></a>
  <a href="https://github.com/OpenSelena/open-nami/releases/latest"><img src="https://img.shields.io/github/v/release/OpenSelena/open-nami?style=for-the-badge&label=Open%20Nami&color=8b5cf6" alt="Open Nami" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2AA845?style=for-the-badge" alt="License MIT" /></a>
</p>

## Getting Started

Add the OpenSelena tap to your Homebrew installation:

```bash
brew tap OpenSelena/tap
```

## Available Tools

### 1. LibreGet (Desktop App)
Universal desktop media downloader and tool hub for macOS (Apple Silicon & Intel).
```bash
brew install --cask libreget
```

### 2. Open Omni (CLI)
Terminal media downloader and TUI for 1,800+ sites with batch playlist processing.
```bash
brew install open-omni
```

### 3. Open Nami (CLI)
Bulk creator media profile archiver for Instagram, TikTok, Facebook, and X.
```bash
brew install open-nami
```

## Updating

Update all tools installed from this tap with standard Homebrew commands:

```bash
# Update tap manifests
brew update

# Upgrade LibreGet desktop app
brew upgrade --cask libreget

# Upgrade CLI tools
brew upgrade open-omni open-nami
```

## Repositories & Documentation

- **[LibreGet](https://github.com/OpenSelena/libreget)** — Desktop media downloader & 158-tool hub
- **[LibreGet Extension](https://github.com/OpenSelena/libreget-extension)** — Companion browser extension for Chrome, Edge, and Firefox
- **[Open Omni](https://github.com/OpenSelena/openomni)** — Terminal media downloader & TUI
- **[Open Nami](https://github.com/OpenSelena/open-nami)** — Bulk creator profile archiver

For tap-specific packaging issues or cask requests, visit the [homebrew-tap issue tracker](https://github.com/OpenSelena/homebrew-tap/issues).

## License

MIT License. See [LICENSE](LICENSE) for details.

Maintained by [Igect](https://github.com/igect) under the [OpenSelena](https://github.com/OpenSelena) organization.
