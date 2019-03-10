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
            self.exception_handle2()
            return Appium.getDriver().find_element(by, value)

    def find(self, locate):
        return self.findBy(*locate)

    def exception_handle(self):
        for w in self.black_words:
            elements = Appium.getDriver().find_elements(By.XPATH, w)
            if len(elements) > 0:
                elements[0].click()
                return Appium.getDriver().find_element(by, value)

    def exception_handle2(self):
        page_source=Appium.getDriver().page_source
        print(page_source)
        #parser = etree.XMLParser(encoding='utf-8')
        xml=etree.XML(str(page_source).encode("utf-8"))
        for w in self.black_words:
            print(w)
            if(len(xml.xpath(w))>0):
                Appium.getDriver().find_element(By.XPATH, w).click()
