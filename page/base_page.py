from lxml.html import Element
from selenium.webdriver.common.by import By

from driver.Appium import Appium
from lxml import etree

class BasePage(object):
    black_words=[ "//*[@text='好的']"]
    def findBy(self, by=By.ID, value=None):
        try:
            return Appium.getDriver().find_element(by, value)
        except:
            for w in self.black_words:
                elements=Appium.getDriver().find_elements(By.XPATH, w)
                if len(elements)>0:
                    elements[0].click()
                    return Appium.getDriver().find_element(by, value)
            # page_source=Appium.getDriver().page_source
            # print(page_source)
            # xml=etree.HTML(page_source)
            # for w in self.black_words:
            #     print(w)
            #     if(len(xml.xpath(w))>0):
            #         Appium.getDriver().find_element(By.XPATH, w).click()



    def find(self, locate):
        return self.findBy(*locate)
