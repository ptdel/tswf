import sys
import pytest
from pathlib import Path


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))

from player import Stream