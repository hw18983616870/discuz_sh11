"""
============================
@author:多测师-黄sir
@time:2021/3/13:9:11
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
import unittest
from public.pages.BasePage import BasePage
from public.pages.discuz_login_ele import Test_login as tl
from public.utils.ReadDataIni import *
from selenium import webdriver
from time import sleep
class Test_Discuz_Login(BasePage):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        BasePage.set_driver(self.driver)

    def test01(self):
        driver = BasePage.get_driver()  #拿到BasePage模块的driver对象
        driver.get(url)
        BasePage.maxwindow()

        # 1.输入用户名
        BasePage.find_element(tl.user_ele)
        BasePage.sendkeys(username)
        # 2.输入密码
        BasePage.find_element(tl.pwd_ele)
        BasePage.sendkeys(pwd)
        # 3.点击登录按钮
        BasePage.find_element(tl.button_ele)
        BasePage.clickele()
        sleep(2)

        # 4.断言
        BasePage.find_element(tl.loginout_ele)
        assert BasePage.get_text() == "退出"
        # value = BasePage.get_text()
        # print(value)
if __name__ == '__main__':
    unittest.main()