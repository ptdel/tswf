
import sys
import pytest
import httpretty
from pathlib import Path

base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "api"))

from api.skip import Skip


#: Fixtures 

httpretty.register_uri(httpretty.GET, "http://127.0.0.1:8081/restart")
#: Tests

def test_skip_ip():
        test_skip = Skip()
        test_skip.ip_whitelist = ["1.2.3.4"]
        with pytest.raises(Exception, match=r"403 Forbidden"):
            test_skip("test","5.6.7.8")

def test_skip_votes():
    test_skip = Skip()
    test_skip.ip_whitelist = ["1.2.3.4"]
    test_skip.votecount = 5
    test_skip.append("test")
    httpretty.enable()
    r = test_skip("test2", "1.2.3.4")
    httpretty.disable()
    
