from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search import Search


class Portfolio(BasePage):
    _search_button=(By.ID, "action_create_cube")
    def toSearch(self):
        self.find(self._search_button).click()
        return Search()