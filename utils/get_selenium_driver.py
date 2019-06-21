# -*- coding:utf-8 -*-
from selenium import webdriver
from utils.singleton import singleton
import os
@singleton
class GetSeleniumDriver(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self):#内置初始化代码
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        #self.driver = webdriver.Ie(self.ie_driver_path)