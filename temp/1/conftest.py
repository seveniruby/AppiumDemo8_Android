import pytest

@pytest.fixture(scope="module")
def username():
    print("username module 1")
    return "module username 1"