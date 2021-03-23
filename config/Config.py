"""
============================
@author:多测师-黄sir
@time:2021/3/12:15:32
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
'''此模块用来存放当前项目所有的文件和目录的绝对路径'''
import os

# 1.当前项目的绝对路径
path = os.path.dirname(os.path.dirname(__file__))  #获取当前目录的上一级目录的绝对路径
# print(path)         # D:/workspace/discuz_sh11

# 2.config目录的绝对路径
config_path = os.path.join(path,'config')
# print(config_path)   #D:/workspace/discuz_sh11\config

# 3.data目录的绝对路径
data_path = os.path.join(path,'data')

# 4.pubilc目录的绝对路径
pubilc_path = os.path.join(path,'public')

# 5.report目录的绝对路径
report_path = os.path.join(path,'report')

# 6.testcase目录的绝对路径
testcase_path = os.path.join(path,'testcase')

# 7.pages目录的绝对路径
pages_path = os.path.join(data_path,'pages')

# 8.utils目录的绝对路径
utils_path = os.path.join(data_path,'utils')
