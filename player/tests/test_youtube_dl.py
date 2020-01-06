import sys
import pytest
from pathlib import Path
from youtube_dl import YoutubeDL


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))

from ydl import ydl


def test_ydl():
    assert type(ydl) == YoutubeDL
