from driver.Appium import Appium


class Search(object):

    def search(self, keyword):
        Appium.getDriver().find_element_by_id("search_input_text").send_keys(keyword)
        return self

    def getUserName(self):
        Appium.getDriver().find_element_by_xpath("//*[@text='用户']").click()
        return Appium.getDriver().find_element_by_id("user_name").text



    def getStocks(self):
        return Appium.getDriver().find_element_by_id("stockName").text