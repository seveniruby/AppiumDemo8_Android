import pytest
import logging

class TestDemo(object):
    def test_demo1(self, username):
        print(username)

    def test_demo2(self, username11):
        logging.getLogger().info('boo %s', 'arg')
        print(username11)
        logging.info("xxxxx")
        logging.debug("ddd")