import pytest
import unittest
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestApiDemo(unittest.TestCase):
    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        #caps["appPackage"] = "com.example.android.apis"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"
        caps["newCommandTimeout"] = 600

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    def test_toast(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        #self.driver.find_element_by_accessibility_id("Popup Menu").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Popup Menu")'
        ).click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element_by_xpath("//*[@package='com.android.settings']").text)
        print(self.driver.find_element_by_xpath("//*[contains(@text, 'Clicked')]").text)

    def test_toast_not_found(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        #self.driver.find_element_by_accessibility_id("Popup Menu").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Popup Menu")'
        ).click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()


    def test_webview_sim_simple(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "WebView")'
        ).click()
        self.driver.find_element_by_accessibility_id("Hello World! - 1").click()





