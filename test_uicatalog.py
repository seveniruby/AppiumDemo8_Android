# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import unittest
from appium import webdriver
from appium.webdriver.webelement import WebElement


class TestUicatalog(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["platformVersion"] = "12.1"
        caps["deviceName"] = "iPhone X"
        caps["app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphonesimulator/UICatalog.app"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_buttons(self):
        el2 = self.driver.find_element_by_accessibility_id("Buttons")
        el2.click()
        print(self.driver.page_source)
        self.driver.find_element_by_accessibility_id("UICatalog").click()

    def tearDown(self):
        self.driver.quit()