import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

from settings import audio_folder, video_folder
from common import replace_ext, list_dir


def video2audio():
    for video_path in list_dir(video_folder, ['.mp4', '.mkv', '.wmv']):
        video_name = os.path.basename(video_path)
        audio_output_path = os.path.join(audio_folder, replace_ext(video_name, 'mp3'))
        if not os.path.exists(audio_output_path):
            ffmpeg_extract_audio(video_path, audio_output_path)


if __name__ == '__main__':
    video2audio()