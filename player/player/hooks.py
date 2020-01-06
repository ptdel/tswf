from player import stream

def download_hook(data, stream=stream):
    if data["status"] == "finished":
        stream.stream_song(data["filename"])
