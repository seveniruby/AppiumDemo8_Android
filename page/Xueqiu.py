from selenium.webdriver.common.by import By

from driver.Appium import Appium
from page.base_page import BasePage
from page.Search import Search


class Xueqiu(BasePage):
    _search=(By.ID, "home_search")
    def toSearch(self):
        self.find(self._search).click()
        return Search()