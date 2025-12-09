# backend/settings.py
from pathlib import Path
import os

# RunPod automatically mounts volume here for Serverless
VOLUME_ROOT = Path("/runpod-volume")

# Directory layout on the volume
INPUT_DIR = VOLUME_ROOT / "input"
BOOKS_DIR = VOLUME_ROOT / "audiobooks"

# TTS config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set")
