import unittest
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page.Search import Search
from driver.Appium import Appium
from page.Xueqiu import Xueqiu


class TestXueqiu(unittest.TestCase):
    loaded = False

    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)


    def test_add_stock(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.save_screenshot("screenshot/tv_search.png")
        self.driver.find_element_by_id("search_input_text").send_keys("pdd")
        self.driver.save_screenshot("screenshot/search_input_text.png")

        print(self.driver.find_element_by_id("add_attention") \
              .find_element_by_class_name("android.widget.TextView") \
              .get_attribute("resourceId"))

        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    def test_check_stock(self):
        for i in range(1, 5):
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            print(element.location)
            element.text
            element.get_attribute("text")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id, 'portfolio_stockName') and @text='拼多多']"))

    def test_mobile(self):
        # self.driver.start_activity("com.android.calculator2", ".Calculator")
        print(self.driver.is_locked())
        self.driver.lock(5)
        self.driver.unlock()
        # self.driver.shake()

    def test_touch(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()

        element = self.driver.find_element_by_xpath("//*[@text='拼多多']")
        TouchAction(self.driver).long_press(element).perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").click()

    def test_main_swipe(self):
        self.loaded()
        for i in range(1, 10):
            sleep(1)
            self.driver.swipe(start_x=1340, start_y=2000, end_x=200, end_y=600, duration=1000)

    def find(self, by, locator):
    
        try:
            self.driver.find_element(by, locator)
        except:
            keywords=[]
            for key in keywords:
                elements=self.driver.find_elements(key)
                if len(elements)>0:
                    elements[0].click()


    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            locations.append(element.location)
            print(locations)

    def test_battery(self):
        print(self.driver.execute_script("mobile:batteryInfo"))

    def test_shell(self):
        print(self.driver.execute_script("mobile:shell",
                                         {"command": "am",
                                          "args": ["start", "-n", "com.android.calculator2/.Calculator"]}))

    def test_webview_sim_image(self):
        self.loaded()
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        self.driver.find_element_by_accessibility_id("15da75b0b28c2b23feda8fe7").click()


    def test_webview_sim_h5(self):
        self.loaded()
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.ACCESSIBILITY_ID, "基金开户")))
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print(self.driver.current_context)
        print(self.driver.page_source)
        self.driver.find_element_by_css_selector(".trade_home_agu_3ki").click()

    def test_search(self):
        xueqiu=Xueqiu()
        search=xueqiu.toSearch()
        search.search("pdd")
        assert search.getStocks() == "拼多多"

    def test_search_username(self):
        xueqiu=Xueqiu()
        search=xueqiu.toSearch()
        search.search("seveniruby")
        assert search.getUserName() == "seveniruby"








