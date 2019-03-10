from unittest import TestCase

from page.stock_group import StockGroup
import pytest

from page.xueqiu import Xueqiu


class TestStockGroup(object):

    def setup(self):
        # todo: 删除所有分组
        self.group = StockGroup()
        pass

    def test_add(self):
        self.group.add("demo")
        assert "demo" in self.group.getGroups()

    @pytest.mark.parametrize("group,name", [
        ("g1", "n1"),
        ("g2", "n2"),
        ("g3", "n3")
    ])
    def test_add(self, group, name):
        self.group.toGroup(group)
        self.group.add(name)
        assert name in self.group.getGroups()

    @pytest.mark.parametrize("name", ["1", "demo2", "中文名"])
    def test_delete(self, name):
        name = "demo2"
        assert name in self.group.add(name).getGroups()
        self.group.delete(name)
        assert name not in self.group.getGroups()
