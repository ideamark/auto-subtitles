import os
import json

from settings import json_folder, output_folder
from common import replace_ext, seconds_to_time, generate_srt


def json2srt():
    for json_name in os.listdir(json_folder):
        if json_name.endswith('.json'):
            srt_path = os.path.join(output_folder, replace_ext(json_name, 'srt'))
            json_path = os.path.join(json_folder, json_name)
            subtitles = []
            with open(json_path, 'r') as fp:
                data = json.load(fp)
                for segment in data['segments']:
                    start_time = seconds_to_time(segment['start'])
                    end_time = seconds_to_time(segment['end'])
                    text = segment['text']
                    subtitles.append({'start_time': start_time, 'end_time': end_time, 'text': text})
                generate_srt(srt_path, subtitles)
    

if __name__ == '__main__':
    json2srt()