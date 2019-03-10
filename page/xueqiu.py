from selenium.webdriver.common.by import By

from driver.Appium import Appium
from page.base_page import BasePage
from page.portfolio import Portfolio
from page.search import Search
from page.stock import Stock


class Xueqiu(BasePage):
    _search=(By.ID, "home_search")
    _portfolio=(By.XPATH,"//*[@text='自选' and contains(@resource-id, 'tab_name')]")
    def __init__(self):
        self.loaded()

    def toSearch(self):
        self.find(self._search).click()
        return Search()

    def toPortfolio(self):
        self.find(self._portfolio).click()
        return Stock()

    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.find(self._portfolio)
            print(element)
            locations.append(element.location)
            print(locations)