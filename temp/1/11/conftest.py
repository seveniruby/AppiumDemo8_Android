import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope="class")
def username11():
    print("username 11 module 11")
    return "module username 11"