# Audiobook Platform — Master Plan

## Project Goal
A personal, learning-oriented audiobook system that:
- Converts ebooks into high-quality audiobooks offline
- Preserves perfect paragraph-level sync
- Serves audiobooks via static hosting
- Is audio-first and translation-ready in the future

This project prioritizes correctness, clarity, and durability over speed or scale.

## Non-Goals
- No real-time TTS
- No streaming generation
- No user accounts or payments
- No DRM
- No mobile apps (for now)

## Architectural Principles
- Offline generation, online playback
- Immutable generation artifacts
- Static-first serving (CDN-ready)
- Clear phase boundaries

## Phase Lock
Phases 1 and 2 are complete and MUST NOT be modified.
All future work must build on top of their outputs.

## Future UI Expansion
UI complexity is expected to grow.
UI-related documentation will be added only when real complexity emerges.
