from pathlib import Path
import os

# Network Volume mount path for Secure Cloud Pods
VOLUME_ROOT = Path("/workspace")

INPUT_DIR = VOLUME_ROOT / "input"
BOOKS_DIR = VOLUME_ROOT / "audiobooks"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing")
