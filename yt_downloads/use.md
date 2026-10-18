This is to set file path to download in particular path --
python download_playlist.py "https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1&si=iU2sv5sYIDfeNZGm" -o my_videos


# YouTube Playlist Downloader (720p)

A simple Python script that downloads an entire YouTube playlist in up to 720p quality, with audio and video merged in sync into MP4 files. Built on [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [ffmpeg](https://ffmpeg.org/).

## Features

- Downloads full playlists at up to 720p
- Prefers H.264 video and AAC audio for best compatibility and sync
- Resets timestamps while merging to prevent audio/video drift
- Saves files in playlist order (`01 - Title.mp4`) inside a folder named after the playlist
- Skips unavailable or private videos instead of stopping
- Retries failed downloads automatically

## Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (must be on your PATH)

## Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>

# Optional: create a virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -U yt-dlp
```

Install ffmpeg:

| OS      | Command                    |
|---------|----------------------------|
| Windows | `winget install ffmpeg`    |
| macOS   | `brew install ffmpeg`      |
| Linux   | `sudo apt install ffmpeg`  |

## Usage

```bash
python download_playlist.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

Choose a custom output folder:

```bash
python download_playlist.py "YOUR_PLAYLIST_URL" -o my_videos
```

Videos are saved to `downloads/<playlist title>/` by default.

## Troubleshooting

- **`ffmpeg not found`**: install ffmpeg and restart your terminal or editor.
- **Downloads fail or break**: update yt-dlp with `pip install -U yt-dlp`, since YouTube changes often.
- **`python` not recognized**: try `py` (Windows) or `python3` (macOS/Linux).
- **Keep the quotes around the URL**, or the `&` character can break the command.

## Disclaimer

This tool is for personal use. Only download content you have the right to save. Downloading videos may violate YouTube's Terms of Service, and you are responsible for how you use this script.

## License

MIT--If needed.