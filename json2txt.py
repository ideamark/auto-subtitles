import os
import json

from settings import json_folder, output_folder
from common import replace_ext, seconds_to_time, generate_srt


def json2txt():
    for json_name in os.listdir(json_folder):
        if json_name.endswith('.json'):
            txt_path = os.path.join(output_folder, replace_ext(json_name, 'txt'))
            json_path = os.path.join(json_folder, json_name)
            lines = []
            with open(json_path, 'r') as fp:
                data = json.load(fp)
                for segment in data['segments']:
                    text = segment['text']
                    lines.append(text + '\n')
            with open(txt_path, 'w') as fp:
                fp.writelines(lines)
    

if __name__ == '__main__':
    json2txt()