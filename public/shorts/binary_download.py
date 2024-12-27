import requests
import tarfile
import os

# Download the file
url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
response = requests.get(url, stream=True)
with open("ffmpeg-release-amd64-static.tar.xz", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# Extract the downloaded archive
with tarfile.open("ffmpeg-release-amd64-static.tar.xz", "r:xz") as tar:
    tar.extractall()

# Once extracted, you can set the path to ffmpeg as previously mentioned.
os.environ['IMAGEIO_FFMPEG_EXE'] = './ffmpeg-git-<date>-amd64-static/ffmpeg'
