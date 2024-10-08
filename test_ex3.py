import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("1+7", 8, marks=pytest.mark.basic),
        pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
        pytest.param(
            "6*9", 54, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"
        ),
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# A test that's expected to fail.
@pytest.mark.xfail(reason="Expected to fail until we fix the bug.")
def test_example_xfail():
    assert 2 * 3 == 7

@pytest.mark.xfail(reason="Expected to fail until we fix the bug.")
def test_example_xpass():
    assert 3 * 2 == 6
