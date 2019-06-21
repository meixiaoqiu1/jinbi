# -*- coding:utf-8 -*-
from utils.get_selenium_driver import GetSeleniumDriver
from utils.read_excel_data import  ReadExcelData
import unittest,time
class GetUrl(unittest.TestCase):
    url=ReadExcelData().returnExcelData('data.xlsx', 'index', 0,1)
    driver.get(url)
    time.sleep(1)
    self.driver.maximize_window()