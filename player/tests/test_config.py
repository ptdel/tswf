import sys
import pytest
from pathlib import Path


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))

from log import Logger
from hooks import download_hook
from config import ydl_opts

def test_options():
    opts = ydl_opts

    assert opts["format"] == "bestaudio/best"
    assert opts["outtmpl"] == "/songs/%(title)s.%(ext)s"
    assert opts["postprocessors"] == [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }
    ]
    assert type(opts["logger"]) == Logger
    assert opts["progress_hooks"] == [download_hook]