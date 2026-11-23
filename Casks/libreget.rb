cask "libreget" do
  version "1.0.0"

  on_arm do
    url "https://github.com/OpenSelena/libreget/releases/download/v#{version}/LibreGet_#{version}_aarch64.dmg"
    sha256 "26e6e68f929e6179922cefcc2a20d4f15b668cbc13719c9aab5ecddc79c291bb"
  end
  on_intel do
    url "https://github.com/OpenSelena/libreget/releases/download/v#{version}/LibreGet_#{version}_x64.dmg"
    sha256 "75f2b6c6ff8051f834074bdaa8c66149bbae4952d80de6a21a6c10ec7101f38e"
  end

  name "LibreGet"
  desc "Universal media downloader and tool hub"
  homepage "https://github.com/OpenSelena/libreget"

  livecheck do
    url :url
    strategy :github_latest
  end

  app "LibreGet.app"

  zap trash: [
    "~/Library/Application Support/com.openselena.libreget",
    "~/Library/Caches/com.openselena.libreget",
    "~/Library/Preferences/com.openselena.libreget.plist",
    "~/Library/Saved Application State/com.openselena.libreget.savedState",
  ]
end
