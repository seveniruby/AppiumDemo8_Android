import unittest
from appium import webdriver

class TestH5(unittest.TestCase):
    def setUp(self):
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="seveniruby"
        #caps["browserName"]="chrome"
        caps["browserName"]="Browser"
        caps["noReset"]="true"
        caps["fullReset"]="false"
        caps["forceMjsonwp"]="true"
        caps["dontStopAppOnReset"]="true"

        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_main(self):

        self.driver.get("https://danjuanapp.com/my-money?channel=1300100158&refer=xq_trade")
        self.driver.find_element_by_css_selector(".btns .blank").click()
        self.driver.find_element_by_css_selector(".pass_switch").click()
        self.driver.find_element_by_name("telno").send_keys("15600534760")
        self.driver.find_element_by_name("pass").send_keys("password")
        self.driver.find_element_by_id("next").click()
