import pytest
import unittest
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestIOS(unittest.TestCase):
    loaded = False

    def setUp(self):
        pass


    def test_uicatalog_sim(self):

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


        print(self.driver.page_source)
        self.driver.find_element_by_id("Buttons").click()
        self.driver.back()
        self.driver.find_element_by_accessibility_id("Buttons").click()

    def test_uicatalog_real_by_url(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["automationName"] = "xcuitest"
        caps["deviceName"] = "Uzumaki的iPhone"
        caps["udid"]="auto"
        caps["app"] = '/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/' \
                      'Build/Products/Debug-iphoneos/UICatalog.app'
        caps["xcodeOrgId"]="96NJEQL7Y2"
        caps["xcodeSigningId"]="iPhone Developer"
        caps["webDriverAgentUrl"]="http://192.168.0.102:8100"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print(self.driver.page_source)

    def test_uicatalog_real(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["automationName"] = "xcuitest"
        caps["deviceName"] = "Uzumaki的iPhone"
        caps["udid"]="auto"
        caps["app"] = '/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/' \
                      'Build/Products/Debug-iphoneos/UICatalog.app'
        caps["xcodeOrgId"]="96NJEQL7Y2"
        caps["xcodeSigningId"]="iPhone Developer"
        #加速，绕过构建
        caps["usePrebuiltWDA"]="true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print(self.driver.page_source)

