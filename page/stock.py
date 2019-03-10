from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from driver.Appium import Appium
from page.portfolio import Portfolio


class Stock(Portfolio):

    _name=(By.ID, "com.xueqiu.android:id/portfolio_stockName")
    _us=(By.XPATH, "//*[@text='美股' and contains(@resource-id, 'text')]")

    _all=Portfolio.byAndroid(text="全部")

    def getNameByUS(self):
        self.find(self._us).click()
        x=[]
        for e in self.findAll(self._name):
            x.append(e.text)
        return x

    def getNameByAll(self):
        self.find(self._all).click()
        x=[]
        for e in self.findAll(self._name):
            x.append(e.text)
        return x

    def getNameByGroup(self, name):
        pass


    def delete(self, name, group_name=""):
        if group_name!="":
            self.find((By.XPATH, self.byAttribute(text=group_name))).click()

        print(Appium.getDriver().page_source)
        element=self.find((MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().resourceId("com.xueqiu.android:id/portfolio_stockName").text("'+name+'")'))
        TouchAction(Appium.getDriver()).long_press(el=element).perform()
        self.find((By.XPATH, self.byAttribute(text='删除'))).click()


