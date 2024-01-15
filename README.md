# auto-subtitles

## Summary

auto-subtitles is a tool for automatically generating movie subtitles.

## Installation

* Download and install [ffmpeg](https://ffmpeg.org/download.html)
* Install python modules: `pip install -r requirements.txt`

## Usage

1. Config `settings.py` to set the input video path: `video_path`
2. Run `run.py`，it will generate srt subtitle files in folder `subtitles`
3. Run `clean.py` to clean up generated files if you want to re-generate.

## Contact

* Author: Mark Yang
* Email: ideamark@qq.com
