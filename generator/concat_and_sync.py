from typing import List, Tuple, Dict
from pydub import AudioSegment


def concat_audio_and_build_sync(
    audio_files: List[str],
    texts: List[str],
    pause_ms: int,
) -> Tuple[AudioSegment, List[Dict]]:
    final_audio = AudioSegment.empty()
    sync_map = []
    silence = AudioSegment.silent(duration=pause_ms)

    for idx, (path, text) in enumerate(zip(audio_files, texts)):
        start = round(len(final_audio) / 1000, 3)

        segment = AudioSegment.from_file(path)
        final_audio += segment

        end = round(len(final_audio) / 1000, 3)

        sync_map.append({
            "paragraph_index": idx,
            "start": start,
            "end": end,
            "text": text,
        })

        if idx != len(audio_files) - 1:
            final_audio += silence

    return final_audio, sync_map
