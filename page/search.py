from appium.webdriver.common.mobileby import MobileBy

from driver.Appium import Appium
from page.base_page import BasePage


class Search(BasePage):
    _user=(MobileBy.XPATH, "//*[@text='用户']")
    _username=(MobileBy.ID, "user_name")
    _stockName = (MobileBy.ID, "stockName")
    _search = (MobileBy.ID, "search_input_text")
    _cancel=(MobileBy.XPATH, "//*[@text='取消']")

    _follow=(MobileBy.ID, "com.xueqiu.android:id/follow_btn")
    _followed = (MobileBy.ID, "com.xueqiu.android:id/followed_btn")

    def search(self, keyword):
        self.find(self._search).send_keys(keyword)
        return self

    def getUserName(self):
        self.find(self._user).click()
        self.find(self._username).text



    def getStocks(self):
        return self.find(self._stockName).text

    def cancel(self):
        self.find(self._cancel).click()

    def followFirst(self):
        elements=self.findAll(self._follow)
        if len(elements)==2:
            elements[0].click()

        return self
