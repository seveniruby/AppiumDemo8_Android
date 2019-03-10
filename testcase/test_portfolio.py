import pytest
import unittest

from driver.Appium import Appium
from page.xueqiu import Xueqiu


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        #todo: 数据的初始化
        Appium.initDriver()
        self.xueqiu=Xueqiu()
        self.stock=self.xueqiu.toPortfolio()

    def test_list(self):
        print(self.stock.getNameByUS())


    def test_add(self):
        self.stock.toSearch().search("alibaba").followFirst().cancel()
        assert "阿里巴巴" in self.stock.getNameByUS()

    def test_delete(self):
        self.stock.delete("拼多多", "美股")
        assert "拼多多" not in self.stock.getNameByUS()

    def test_delete_all(self):

        #todo: xpath定位bug 确认是8.0系统上的android Uiautomator2 server的bug
        #todo: 使用接口清理数据是更高效的办法

        stocks=[]
        while True:
            stocks=self.stock.getNameByAll()
            if len(stocks)==0:
                break
            stock=stocks[0]
            print(stock)
            self.stock.delete(stock)
            #Appium.initDriver()
            #self.xueqiu = Xueqiu()
            #self.stock = self.xueqiu.toPortfolio()

        assert len(self.stock.getNameByAll())==0
