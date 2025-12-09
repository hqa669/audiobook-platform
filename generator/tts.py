import os
from pathlib import Path
from openai import OpenAI
from tqdm import tqdm

DEFAULT_MODEL = "gpt-4o-mini-tts"
DEFAULT_VOICE = "alloy"

def synthesize_paragraphs(paragraphs, output_dir: Path):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_paths = []

    for i, text in enumerate(tqdm(paragraphs)):
        path = output_dir / f"{i:06d}.mp3"
        audio_paths.append(path)

        if path.exists():
            continue

        with client.audio.speech.with_streaming_response.create(
            model=DEFAULT_MODEL,
            voice=DEFAULT_VOICE,
            input=text,
            response_format="mp3",
        ) as response:
            response.stream_to_file(path)

    return audio_paths
