import pytest
import logging

class BaseDemo(object):
    def setup(self):
        logging.basicConfig(level=logging.DEBUG)
        print("setup BaseDemo")

