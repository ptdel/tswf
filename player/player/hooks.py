from player import stream_song
from os import remove


def download_hook(d):
    if d["status"] == "finished":
        stream_song(d["filename"])
