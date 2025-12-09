from pydub import AudioSegment

def build_sync(chunks):
    t = 0.0
    sync = []

    for i, path in enumerate(chunks):
        seg = AudioSegment.from_file(path)
        d = len(seg) / 1000
        sync.append({"paragraph_index": i, "start": t, "end": t + d})
        t += d

    return sync
