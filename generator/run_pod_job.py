import argparse
from pathlib import Path
import json
import shutil

from settings import INPUT_DIR, BOOKS_DIR
from ingest_epub import extract_paragraphs
from tts import synthesize_paragraphs
from concat_and_sync import concat_audio_and_build_sync


def main():
    parser = argparse.ArgumentParser(description="Run audiobook generation job")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--epub", required=True)
    parser.add_argument("--pause-ms", type=int, default=900)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    epub_path = Path(args.epub)
    if not epub_path.exists():
        raise FileNotFoundError(epub_path)

    book_dir = BOOKS_DIR / args.book_id
    chunks_dir = book_dir / "chunks"
    book_dir.mkdir(parents=True, exist_ok=True)

    paragraphs = extract_paragraphs(epub_path, limit=args.limit)

    audio_paths = synthesize_paragraphs(paragraphs, chunks_dir)

    audio, sync = concat_audio_and_build_sync(
        [str(p) for p in audio_paths],
        paragraphs,
        pause_ms=args.pause_ms,
    )

    audio.export(book_dir / "audio.mp3", format="mp3")

    (book_dir / "sync_map.json").write_text(
        json.dumps(sync, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    (book_dir / "paragraphs.json").write_text(
        json.dumps(paragraphs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    shutil.copy2(epub_path, book_dir / "book.epub")
    print(f"✅ Finished book {args.book_id}")


if __name__ == "__main__":
    main()
