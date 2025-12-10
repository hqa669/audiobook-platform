# Implementation Plan

## Phase 1 — Batch Audiobook Generation (COMPLETE)

### Inputs
- EPUB files
- CLI invocation

### Process
- Deterministic paragraph extraction
- Paragraph-level TTS
- Concatenation and sync map generation

### Outputs
For each book-id:

/workspace/audiobooks/{book-id}/
- audio.mp3
- sync_map.json
- paragraphs.json
- chunks/
- book.epub

### Status
Locked. No downstream modification allowed.

---

## Phase 2 — Static Playback Hosting (COMPLETE)

### Hosting
- Static HTTP (python http.server / nginx)
- Served from /workspace

### UI
- reader.html
- index.html
- Paragraph highlight synced to audio

### Status
Locked. Playback only.

---

## Phase 3 — Library & Productization (PLANNED)

### Intended Additions
- Book index (static JSON)
- Multi-book selection UI
- Audio-first refinements

Phase 3 must NOT regenerate or alter Phase 1 artifacts.
