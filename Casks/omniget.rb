cask "omniget" do
  version "0.15.0"

  on_arm do
    url "https://github.com/OpenSelena/omniget/releases/download/v#{version}/OmniGet_#{version}_aarch64.dmg"
    sha256 "62abe692d1809f53beb8b17bf34e6077eb4fb3f9a92d7234e77ac8ca9947f652"
  end
  on_intel do
    url "https://github.com/OpenSelena/omniget/releases/download/v#{version}/OmniGet_#{version}_x64.dmg"
    sha256 "7656e146f5c6a1b0811756741b65ce6ad2d8d7dc0a6fee131f9f21072276d5b8"
  end

  name "OmniGet"
  desc "Universal downloader and media workstation"
  homepage "https://github.com/OpenSelena/omniget"

  livecheck do
    url :url
    strategy :github_latest
  end

  app "OmniGet.app"

  zap trash: [
    "~/Library/Application Support/com.openselena.omniget",
    "~/Library/Caches/com.openselena.omniget",
    "~/Library/Preferences/com.openselena.omniget.plist",
    "~/Library/Saved Application State/com.openselena.omniget.savedState",
  ]
end
