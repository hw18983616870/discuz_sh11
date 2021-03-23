"""
============================
@author:多测师-黄sir
@time:2021/3/12:16:53
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
'''封装所有页面元素的操作方法'''
# 以下两行代码用做调试使用
# from selenium import webdriver
# driver = webdriver.Chrome()

import unittest

class BasePage(unittest.TestCase):
    '''
    单例设计模式
    定义一个打开浏览器的变量，并且要定义成一个类属性
    '''
    @classmethod
    def set_driver(cls,driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver     #把设置的driver变量，通过返回值的方法返回给到函数的调用处

    # baidu_locator = ['id','kw']
    # typ = baidu_locator[0]
    # value = baidu_locator[1]
    @classmethod
    def find_element(cls,element):
        typ = element[0]
        value = element[1]
        if typ =='id':
            cls.ele = cls.driver.find_element_by_id(value)
        elif typ == 'name':
            cls.ele = cls.driver.find_element_by_name(value)
        elif typ == 'class':
            cls.ele = cls.driver.find_element_by_class_name(value)
        elif typ =='xpath':
            cls.ele = cls.driver.find_element_by_xpath(value)
        elif typ == 'css':
            cls.ele = cls.driver.find_element_by_css_selector(value)
        elif typ == 'link':
            cls.ele = cls.driver.find_element_by_link_text(value)
        return cls.ele
    '''输入框输入内容'''
    @classmethod
    def sendkeys(cls,value):
        return cls.ele.send_keys(value)

    '''页面元素点击'''
    @classmethod
    def clickele(cls):
        return cls.ele.click()

    '''窗口最大化'''
    @classmethod
    def maxwindow(cls):
        return cls.driver.maximize_window()

    '''隐式等待'''
    @classmethod
    def wait(cls,sec):
        return cls.ele.implicitly_wait(sec)

    '''获取元素的文本值'''
    @classmethod
    def get_text(cls):
        return cls.ele.text

# if __name__ == '__main__':
#     b = BasePage()
#     b.set_driver(driver)
#     chrome1 = b.get_driver()
#     chrome1.get('http://www.baidu.com')
#     b.maxwindow()
#     baidu_locator = ['id', 'kw']
#     b.find_element(baidu_locator)
#     b.sendkeys('python')