"""
============================
@author:多测师-黄sir
@time:2021/3/12:16:12
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
'''此模块用来读取Data.ini的配置信息'''
# configparser -->此模块用于读取ini配置文件内容
from config.Config import *
from configparser import ConfigParser

ini_path = os.path.join(data_path,'Data.ini')
# print(ini_path)

class ReadDataIni(ConfigParser):
    '''继承父类ConfigParser的构造函数'''
    '''方法1'''
    def __init__(self,filename):
        ConfigParser.__init__(self)  #继承父类的构造函数
        self.read(filename)
    '''方法2'''
    # def __init__(self,filename):
    #     super(ConfigParser, self).__init__()
    #     self.read(filename)
    '''定义一个获取文件内的参数信息的方法'''
    def read_data(self,section,option):
        return self.get(section=section,option=option)

r = ReadDataIni(ini_path)
url = r.read_data(section='discuz_data',option='url')
# print(url)
username = r.read_data(section='discuz_data',option='username')
# print(username)
pwd = r.read_data(section='discuz_data',option='pwd')
# print(pwd)
url1 = r.read_data(section='baidu_data',option='url_baidu')