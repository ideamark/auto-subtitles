# auto-subtitles

## 综述

auto-subtitles 是一款电影字幕自动生成工具。

## 安装

* 下载安装 [ffmpeg](https://ffmpeg.org/download.html)
* 安装Python模块：`pip install -r requirements.txt`

## 使用

1. 配置 `settings.py` 文件，设置原始视频路径 `video_path`
2. 运行 `run.py`，将会自动生成srt格式字幕文件至 `subtitles`文件夹
3. 如果你想清除生成的文件以便重新再生成，运行 `clean.py`

## 联系方式

* 作者：Mark Yang
* 邮箱：ideamark@qq.com
