import os
from datetime import datetime

from settings import video_folder


def get_duration(index):
    start_time = index * 5
    end_time = (index + 1) * 5
    return start_time, end_time


def time_to_seconds(time, time_format='%H:%M:%S,%f'):
    ref_dt = datetime(1900, 1, 1, 0, 0, 0)
    time = datetime.strptime(str(time), time_format) - ref_dt
    return time.seconds + time.microseconds / 1000000


def seconds_to_time(seconds, time_format='{:02d}:{:06.3f}'):
    return time_format.format(int(seconds // 60), seconds % 60)


def clear_folder(folder):
    if os.listdir(folder):
        if os.name == 'nt':
            os.system(f'cd /d "{folder}" & for /d %d in (*) do @rd /s /q "%d" & del /q /f "%d\*" 2>nul')
        else:
            os.system(f'rm -rf {folder}/*')


def replace_ext(filename, new_extension):
    root, _ = os.path.splitext(filename)
    new_filename = f'{root}.{new_extension}'
    return new_filename


def list_dir(folder, extensions=[]):

    def is_file_endswith(file, extensions):
        for extension in extensions:
            if file.endswith(extension):
                return True
        return False

    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if is_file_endswith(file, extensions):
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list


def generate_srt(srt_path, subtitles):
    with open(srt_path, 'w') as fp:
        for i, subtitle in enumerate(subtitles, start=1):
            start_time = subtitle['start_time']
            end_time = subtitle['end_time']
            text = subtitle['text']
            srt = f"{i}\n{start_time} --> {end_time}\n{text}\n\n"
            fp.write(srt)


if __name__ == '__main__':
    print(list_dir(video_folder, ['.mp4', '.avi', '.mkv', '.mov', '.wmv']))