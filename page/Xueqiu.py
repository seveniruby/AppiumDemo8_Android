from selenium.webdriver.common.by import By

from driver.Appium import Appium
from page.base_page import BasePage
from page.Search import Search


class Xueqiu(BasePage):
    _search=(By.ID, "home_search")
    def __init__(self):
        self.loaded()

    def toSearch(self):
        self.find(self._search).click()
        return Search()

    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.find((By.XPATH,"//*[@text='自选' and contains(@resource-id, 'tab_name')]"))
            print(element)
            locations.append(element.location)
            print(locations)