import pytest
import unittest
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestIOS(unittest.TestCase):
    loaded = False

    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "ios"
        caps["platformVersion"] = "12.1"
        caps["deviceName"] = "iPhone X"
        caps["app"] = '/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-ftyzdbgapjmxxobezrnrxsshpdqh/' \
                      'Build/Products/Debug-iphonesimulator/UICatalog.app'

        if TestIOS.loaded == True:
            caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        loaded = True

    def test_uicatalog_sim(self):
        print(self.driver.page_source)
        self.driver.find_element_by_id("Buttons").click()
        self.driver.back()
        self.driver.find_element_by_accessibility_id("Buttons").click()
