import os
import json
import whisper

from settings import audio_folder, json_folder
from common import replace_ext


def audio2json():
    # refer to: https://github.com/openai/whisper
    model = whisper.load_model('base')
    for audio_name in os.listdir(audio_folder):
        if audio_name.endswith('.mp3'):
            audio_path = os.path.join(audio_folder, audio_name)
            result = model.transcribe(audio=audio_path, verbose=True, word_timestamps=True)
            json_path = os.path.join(json_folder, replace_ext(audio_name, 'json'))
            with open(json_path, 'w') as fp:
                json.dump(result, fp)


if __name__ == '__main__':
    audio2json()