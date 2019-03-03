from driver.Appium import Appium
from page.Search import Search


class Xueqiu(object):
    def toSearch(self):
        Appium.getDriver().find_element_by_id("home_search").click()
        return Search()