# Audiobook Platform

Batch EPUB → Audiobook pipeline + static reader.

Architecture:
- generator/: RunPod batch audio generation (paragraph-level TTS)
- static/: static file server (audio + reader)
- templates/: canonical reader HTML copied per book

Playback is 100% static (HTTP range MP3).
No streaming backend.
