import unittest
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page.search import Search
from driver.Appium import Appium
from page.xueqiu import Xueqiu


class TestXueqiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)

    def test_search(self):
        assert Xueqiu().toSearch().search("pdd").getStocks() == "拼多多"

    def test_search_username(self):
        assert Xueqiu()\
                   .toSearch()\
                   .search("seveniruby")\
                   .getUserName() == "seveniruby"






