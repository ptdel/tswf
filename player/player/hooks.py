from player import stream
from os import remove


def download_hook(d):
    if d["status"] == "finished":
        stream(d["filename"])
