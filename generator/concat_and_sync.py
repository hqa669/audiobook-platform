from pydub import AudioSegment

def concat_audio_and_build_sync(audio_files, texts, pause_ms):
    final = AudioSegment.empty()
    sync = []
    silence = AudioSegment.silent(duration=pause_ms)

    for idx, (path, text) in enumerate(zip(audio_files, texts)):
        start = round(len(final) / 1000, 3)
        seg = AudioSegment.from_file(path)
        final += seg
        end = round(len(final) / 1000, 3)

        sync.append({
            "paragraph_index": idx,
            "start": start,
            "end": end,
            "text": text
        })

        if idx != len(audio_files) - 1:
            final += silence

    return final, sync
