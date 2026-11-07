require "language/node"

class OpenNami < Formula
  desc "Terminal-first bulk social media profile downloader for Instagram, TikTok, Facebook & X"
  homepage "https://github.com/OpenSelena/open-nami"
  url "https://registry.npmjs.org/open-nami/-/open-nami-1.9.4.tgz"
  sha256 "934e700751af2af84166cd6fda27b2412967db4ecc6b5d2be295ac8597fe7ef6"
  license "MIT"

  livecheck do
    url :stable
  end

  depends_on "ffmpeg"
  depends_on "gallery-dl"
  depends_on "node"
  depends_on "yt-dlp"

  def install
    system "npm", "install", *Language::Node.std_npm_install_args(libexec)
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end

  test do
    assert_match "Open Nami", shell_output("#{bin}/open-nami --help")
  end
end
