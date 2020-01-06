import sys
import pytest
from pathlib import Path
from unittest.mock import MagicMock


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))

from hooks import download_hook

def test_download_hook():
    stream = MagicMock()
    data = {"status": "finished", "filename":"test"}
    download_hook(data, stream=stream)
    stream.stream_song.assert_called_once_with("test")