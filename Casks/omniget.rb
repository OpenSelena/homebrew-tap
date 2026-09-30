cask "omniget" do
  version "0.10.0"

  on_arm do
    url "https://github.com/OpenSelena/omniget/releases/download/v#{version}/omniget_#{version}_aarch64.dmg"
    sha256 "7e674b1b6038c9d9d676c27b0013b03d53104f0761298717e8aa1574787122cf"
  end
  on_intel do
    url "https://github.com/OpenSelena/omniget/releases/download/v#{version}/omniget_#{version}_x64.dmg"
    sha256 "e8235f02c4d888cdcffa237411ad514bef0dc3428caa8e9d2d51321f1c306aeb"
  end

  name "OmniGet"
  desc "Universal downloader and media workstation"
  homepage "https://github.com/OpenSelena/omniget"

  livecheck do
    url :url
    strategy :github_latest
  end

  app "omniget.app"

  zap trash: [
    "~/Library/Application Support/com.openselena.omniget",
    "~/Library/Caches/com.openselena.omniget",
    "~/Library/Preferences/com.openselena.omniget.plist",
    "~/Library/Saved Application State/com.openselena.omniget.savedState",
  ]
end
