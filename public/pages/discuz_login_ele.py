"""
============================
@author:多测师-黄sir
@time:2021/3/13:9:12
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
class Test_login:
    # 用户名输入框
    user_ele = ('id','ls_username')
    # 密码输入框
    pwd_ele = ('id','ls_password')
    # 登录按钮
    button_ele = ('class','pn')

    #断言
    loginout_ele = ('xpath','//*[@id="um"]/p[1]/a[7]')