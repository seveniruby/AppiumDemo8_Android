import pytest
import unittest
from appium import webdriver
from time import sleep


class TestXueqiu(unittest.TestCase):
    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_add_stock(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("pdd")
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()


    def test_check_stock(self):
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        assert 1==len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id, 'portfolio_stockName') and @text='拼多多']"))


