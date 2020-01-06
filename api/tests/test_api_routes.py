import sys
import pytest
from pathlib import Path

base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "api"))

from api import __main__ as api


#: Fixtures

@pytest.fixture(scope="session")
def test_api():
    api.app.testing = True
    test_api = api.app.test_client()
    yield test_api

#: Tests

def test_route_skip_failure(test_api):
    test_api.get("/api/next")
    r = test_api.get("/api/skip?username=chungus")
    assert r.status_code == 405

def test_route_submit(test_api):
    r = test_api.get("/api/submit?song=test")
    assert r.get_json()["Added"] == "test"
    assert r.status_code == 200

def test_route_submit_fail(test_api):
    r = test_api.get("/api/submit?chungus=amungus")
    assert r.status_code == 400

def test_route_stat(test_api):
    r = test_api.get("/api/stat")
    assert r.get_json()["QueueLen"] == 1
    assert r.status_code == 200

def test_route_queue(test_api):
    r = test_api.get("/api/queue")
    assert r.get_json() == ["test"]
    assert r.status_code == 200

def test_route_next(test_api):
    r = test_api.get("/api/next")
    assert r.get_json()["Next"] == "test"
    assert r.status_code == 200  

def test_route_current(test_api):
    r = test_api.get("/api/current")
    assert r.get_json()["Current"] == "test"
    assert r.status_code == 200

def test_route_skip(test_api):
    r = test_api.get("/api/skip?usename=tester")
    assert r.get_json()["Skip"] == "200"
    assert r.status_code == 200  

def test_route_skip_twice_failure(test_api):
    test_api.get("/api/skip?username=tester")
    r = test_api.get("/api/skip?username=tester")
    assert r.status_code == 403

def test_route_clear(test_api):
    r = test_api.get("/api/clear")
    assert r.get_json()["Cleared"] == "playlist"
    assert r.status_code == 200