from pathlib import Path
import json

from ingest_epub import extract_paragraphs
from tts import synthesize_paragraphs
from concat_and_sync import concat_audio_and_build_sync

EPUB = Path("book.epub")
OUT = Path("output")
CHUNKS = OUT / "chunks"

def main():
    paragraphs = extract_paragraphs(EPUB, limit=100)
    paths = synthesize_paragraphs(paragraphs, CHUNKS)

    audio, sync = concat_audio_and_build_sync(
        [str(p) for p in paths],
        paragraphs,
        pause_ms=900,
    )

    OUT.mkdir(exist_ok=True)
    audio.export(OUT / "audio.mp3", format="mp3")
    (OUT / "sync_map.json").write_text(json.dumps(sync, indent=2))

if __name__ == "__main__":
    main()
