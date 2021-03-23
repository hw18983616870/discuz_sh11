"""
============================
@author:多测师-黄sir
@time:2021/3/12:17:27
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
import unittest
from selenium import webdriver
from public.pages.BasePage import BasePage
from public.utils.ReadDataIni import *
from public.pages.Baidu_Element import Baidu_Element as be
class Test_baidu(BasePage):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        BasePage.set_driver(cls.driver)

    def test01(self):
        driver = BasePage.get_driver()
        driver.get(url1)
        BasePage.find_element(be.baidu_input)
        BasePage.sendkeys(be.baidu_value)
if __name__ == '__main__':
    unittest.main()