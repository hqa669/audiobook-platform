import os
import json
from pathlib import Path
import runpod

from ingest_epub import extract_paragraphs
from tts import synthesize_paragraphs
from concat_and_sync import concat_audio_and_build_sync

VOLUME = Path("/runpod-volume")

def handler(job):
    book_id = job["input"]["book_id"]
    epub_path = VOLUME / job["input"]["epub_path"]

    book_dir = VOLUME / "audiobooks" / book_id
    chunks = book_dir / "chunks"

    paragraphs = extract_paragraphs(epub_path)
    paths = synthesize_paragraphs(paragraphs, chunks)

    audio, sync = concat_audio_and_build_sync(
        [str(p) for p in paths],
        paragraphs,
        pause_ms=900,
    )

    book_dir.mkdir(parents=True, exist_ok=True)
    audio.export(book_dir / "audio.mp3", format="mp3")
    (book_dir / "sync_map.json").write_text(json.dumps(sync, indent=2))

    return {"status": "ready", "book_id": book_id}

runpod.serverless.start({"handler": handler})
