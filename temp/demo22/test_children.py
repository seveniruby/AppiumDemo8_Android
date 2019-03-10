import pytest

from temp.demo2.BaseDemo import BaseDemo
import yaml
import logging


def get_data():
    return yaml.load(open("1.yaml", 'r'))


class TestChildren(BaseDemo):
    def setup(self):
        super().setup()
        print("setup Children")
        self.data=[(1, 2), (3, 4)]

    def test_demo(self):
        print("demo")

    @pytest.mark.parametrize("a, b", get_data())
    def test_data(self, a, b):
        logging.info(b)
        print(a)


