import test_pytest

#start with test keyword or end with test keyword

def test_language():
    a = 2
    b = 2
    assert a == b, "test failed"
    assert a+1 == b, "test failed"


def test_browser():
    name = "Katha"
    assert name.upper() == "KATHA"
