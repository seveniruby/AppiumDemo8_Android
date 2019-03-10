import pytest
import logging
import time

logging.basicConfig(level=logging.DEBUG)
loger=logging.getLogger("xxx")
class TestDemo(object):

    def test_1(self):
        log = logging.getLogger('test_1')
        time.sleep(1)
        log.debug('after 1 sec')
        time.sleep(1)
        log.debug('after demo2 sec')
        time.sleep(1)
        log.debug('after 3 sec')
        assert 1, 'should pass'


