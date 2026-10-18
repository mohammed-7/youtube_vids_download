#!/usr/bin/env python3
"""
Download a YouTube playlist in 720p with synced audio and video.

Requirements:
    pip install -U yt-dlp
    ffmpeg installed and on PATH (needed to merge video + audio streams)

Usage:
    python download_playlist.py "https://www.youtube.com/playlist?list=XXXX"
    python download_playlist.py "<playlist_url>" -o my_folder
"""

import argparse
import shutil
import sys

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp is not installed. Run: pip install -U yt-dlp")


def download_playlist(url: str, output_dir: str = "downloads") -> None:
    if shutil.which("ffmpeg") is None:
        sys.exit(
            "ffmpeg not found. Install it first:\n"
            "  Windows: winget install ffmpeg\n"
        )

    ydl_opts = {
        # Prefer H.264 video + AAC audio at max 720p (best compatibility and sync),
        # then fall back to any 720p-or-lower video + best audio, then a single file.
        "format": (
            "bestvideo[height<=720][vcodec^=avc1]+bestaudio[acodec^=mp4a]/"
            "bestvideo[height<=720]+bestaudio/"
            "best[height<=720]"
        ),
        # Merge into MP4 using ffmpeg
        "merge_output_format": "mp4",
        # Keep playlist order in filenames: 01 - Title.mp4
        "outtmpl": f"{output_dir}/%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s",
        # Fix timestamps during merge to avoid A/V drift
        "postprocessor_args": {
            "merger": ["-avoid_negative_ts", "make_zero", "-fflags", "+genpts"],
        },
        # Robustness
        "ignoreerrors": True,        # skip unavailable/private videos
        "retries": 10,
        "fragment_retries": 10,
        "concurrent_fragment_downloads": 4,
        "noplaylist": False,
        "yes_playlist": True,
        "restrictfilenames": False,
        "windowsfilenames": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a YouTube playlist in 720p.")
    parser.add_argument("url", help="YouTube playlist URL")
    parser.add_argument("-o", "--output", default="downloads", help="Output folder (default: downloads)")
    args = parser.parse_args()

    download_playlist(args.url, args.output)
    print("\nDone!")


if __name__ == "__main__":
    main()