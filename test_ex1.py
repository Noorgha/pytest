import pytest


@pytest.fixture
def fixt(request):
    return request.param * 3


@pytest.mark.parametrize("fixt", ["a", "b"], indirect=["fixt"])
def test_indirect(fixt):
    assert len(fixt) == 3