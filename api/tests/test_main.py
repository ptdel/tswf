import sys
import pytest
from unittest import mock
from unittest.mock import MagicMock
from pathlib import Path

base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "api"))

from api import __main__ as api

#: Fixtures

@pytest.fixture(scope="session")
def test_api():
    api.app.testing = True
    api.app.run = MagicMock()
    yield api


#: Tests

def test_initialization(test_api):
    with mock.patch.object(test_api, "app", return_value=0):
        with mock.patch.object(test_api, "__name__", "__main__"):
            test_api.app.run(host="127.0.0.1", port=8080, debug=True)
            test_api.app.run.assert_called_once_with(host="127.0.0.1", port=8080, debug=True)