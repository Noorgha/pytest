import time
import pytest



@pytest.mark.fast
def test_fast_add():
    result = 2+2
    assert result == 4  # Asserting that the result is correct.


# Marked as a 'slow' test due to the intentional delay, this function tests the
# subtraction method of the Calculator.
@pytest.mark.slow
def test_slow_subtraction():
    time.sleep(5)
    result = 10 - 5
    assert result == 5