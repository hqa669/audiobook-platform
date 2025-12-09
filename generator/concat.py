from pydub import AudioSegment
from pathlib import Path

def concatenate_audio(paths, output: Path, silence_ms=900):
    silence = AudioSegment.silent(duration=silence_ms)
    audio = AudioSegment.empty()

    for i, p in enumerate(paths):
        seg = AudioSegment.from_file(p)
        audio += seg
        if i != len(paths) - 1:
            audio += silence

    output.parent.mkdir(parents=True, exist_ok=True)
    audio.export(output, format="mp3")
