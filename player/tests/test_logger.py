import sys
import pytest
from pathlib import Path


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))

from log import Logger

def test_logger():
    l = Logger()
    assert l.debug("yep") == None
    assert l.warning("yep") == None
    assert l.error("yep") == None