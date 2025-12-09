# backend/run_pod_job.py
import argparse
from pathlib import Path

from backend.pipeline import run_pipeline
from backend.settings import INPUT_DIR


def main():
    parser = argparse.ArgumentParser(description="Run audiobook generation job")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--epub", required=True)

    args = parser.parse_args()

    epub_path = Path(args.epub)
    if not epub_path.exists():
        raise FileNotFoundError(epub_path)

    run_pipeline(
        epub_path=epub_path,
        book_id=args.book_id,
    )


if __name__ == "__main__":
    main()
