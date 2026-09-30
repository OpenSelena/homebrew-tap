require "language/node"

class OpenNami < Formula
  desc "Terminal-first bulk social media profile downloader for Instagram, TikTok, Facebook & X"
  homepage "https://github.com/OpenSelena/open-nami"
  url "https://registry.npmjs.org/open-nami/-/open-nami-1.0.2.tgz"
  sha256 "6e0007565fd5a9562c3977bb4ea9dc8622a5a187523c54c8cdd01e8c0bdda39f"
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
