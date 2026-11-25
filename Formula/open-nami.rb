class OpenNami < Formula
  desc "Bulk social media profile downloader for Instagram, TikTok, Facebook & X"
  homepage "https://github.com/OpenSelena/open-nami"
  url "https://registry.npmjs.org/open-nami/-/open-nami-1.9.7.tgz"
  sha256 "b07771db516e08490bf05492b0ad1394d24ed2629a3da8bfb2e2bb626ddb5490"
  license "MIT"

  livecheck do
    url :stable
  end

  depends_on "ffmpeg"
  depends_on "gallery-dl"
  depends_on "node"
  depends_on "yt-dlp"

  def install
    system "npm", "install", *std_npm_args
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end

  test do
    assert_match "Open Nami", shell_output("#{bin}/open-nami --help")
  end
end
