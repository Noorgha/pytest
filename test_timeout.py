import pytest
import time


# A Slow Running Test that's expected to timeout.
@pytest.mark.timeout(10)
def test_timeout():
    #time.sleep(30)
    time.sleep(4)
    assert 2 * 3 == 6
