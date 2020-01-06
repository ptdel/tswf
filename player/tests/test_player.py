import sys
import pytest
from pathlib import Path
from boddle import boddle



base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "player"))