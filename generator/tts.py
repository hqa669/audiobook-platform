from pathlib import Path
from typing import List
from openai import OpenAI
from tqdm import tqdm

from settings import OPENAI_API_KEY

MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"


def synthesize_paragraphs(
    paragraphs: List[str],
    output_dir: Path,
) -> List[Path]:
    client = OpenAI(api_key=OPENAI_API_KEY)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_paths: List[Path] = []

    for idx, text in enumerate(tqdm(paragraphs, desc="TTS paragraphs")):
        path = output_dir / f"{idx:06d}.mp3"
        audio_paths.append(path)

        if path.exists():
            continue

        with client.audio.speech.with_streaming_response.create(
            model=MODEL,
            voice=VOICE,
            input=text,
            response_format="mp3",
        ) as response:
            response.stream_to_file(path)

    return audio_paths
