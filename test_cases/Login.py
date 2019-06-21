# -*- coding:utf-8 -*-
from utils.get_selenium_driver import GetSeleniumDriver
from utils.read_excel_data import  ReadExcelData
from pages.index_page import IndexPage
from pages.login_page import  LoginPage
from common_method.common_def import CommonDef
from utils.logger import  Logger
mylogger = Logger(__name__).getlog()
import unittest,time,os
class Login(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
        cls.driver = GetSeleniumDriver().driver
     @classmethod
     def tearDownClass(cls):
        cls.driver.quit()
     def setUp(self):
        url=ReadExcelData().returnExcelData('data.xlsx', 'index', 0,1)
        self.driver.get(url)
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        IndexPage().click_login_link().click()
        time.sleep(1)
     def tearDown(self):
         self.driver.delete_all_cookies()
     def test01(self):
        mylogger.debug("执行用例：用户名为空，密码正确")
         #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',2,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',2,2)
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(5)
        try:
            error = self.driver.find_element_by_class_name("error").text
            self.assertEqual(error,u"请输入注册手机号/会员账号")
            mylogger.debug("test01执行结果：成功")
        except Exception as e:
            mylogger.debug("test01执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test01")

     def test02(self):
        mylogger.debug("执行用例：用户名31位，判断最多输入30位")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',3,1)
        username2=ReadExcelData().returnExcelData('data.xlsx', 'login',3,3)
        LoginPage().click_username().send_keys(username)
        time.sleep(2)
        try:
            username1=self.driver.find_elements_by_tag_name('input')[0].get_attribute('value')
            self.assertEqual(username1,username2)
            mylogger.debug("test02执行结果：成功")
        except Exception as e:
            mylogger.debug("test02执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test02")
     def test03(self):
        mylogger.debug("执行用例：用户名30位，判断最多输入30位")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',4,1)
        username2=ReadExcelData().returnExcelData('data.xlsx', 'login',4,3)
        LoginPage().click_username().send_keys(username)
        time.sleep(2)
        try:
            username1=self.driver.find_elements_by_tag_name('input')[0].get_attribute('value')
            self.assertEqual(username1,username2)
            mylogger.debug("test03执行结果：成功")
        except Exception as e:
            mylogger.debug("test03执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test03")
     def test04(self):
        mylogger.debug("执行用例：用户名前有空格")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',5,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',5,2)
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(5)
        #判断是否登录成功
        try:
            username2 = self.driver.find_element_by_partial_link_text(username.strip()).text
            self.assertEqual(username2,username.strip(),"登录成功")
            mylogger.debug("test04执行结果：成功")
        except Exception as e:
            mylogger.debug("test04执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test04")
     def test05(self):
        mylogger.debug("执行用例：用户名后有空格")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',6,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',6,2)
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)
        #判断是否登录成功
        username2 = self.driver.find_element_by_partial_link_text(username.strip()).text
        self.assertEqual(username2,username.strip(),"登录成功")
        mylogger.debug("test05执行结果：成功")
        # #判断是否登录成功
        # try:
        #     username2 = self.driver.find_element_by_partial_link_text(username.strip()).text
        #     self.assertEqual(username2,username,"登录成功")
        #     mylogger.debug("test05执行结果：成功")
        # except Exception as e:
        #     mylogger.fail("test05执行结果：失败")
        #     mylogger.fail(e)
        #     CommonDef().get_windows_img("img_test05")
     def test06(self):
        mylogger.debug("执行用例：用户名中间有空格")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',7,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',7,2)
        LoginPage().click_password().send_keys(password)
        time.sleep(2)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)
        try:
            error = self.driver.find_element_by_class_name("error").text
            excError=ReadExcelData().returnExcelData('data.xlsx', 'login',7,3)
            self.assertEqual(error,excError)
            mylogger.debug("test06执行结果：成功")
        except Exception as e:
            mylogger.debug("test06执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test06")

     def test07(self):
        mylogger.debug("执行用例：密码为空")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',8,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',8,2)
        LoginPage().click_password().send_keys(password)
        time.sleep(2)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)
        try:
            error = self.driver.find_element_by_class_name("error").text
            excError=ReadExcelData().returnExcelData('data.xlsx', 'login',8,3)
            self.assertEqual(error,excError)
            mylogger.debug("test07执行结果：成功")
        except Exception as e:
            mylogger.debug("test07执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test07")

     def test08(self):
        mylogger.debug("执行用例：密码错误")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',9,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',9,2)
        LoginPage().click_password().send_keys(password)
        time.sleep(2)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)
        try:
            error = self.driver.find_element_by_class_name("error").text
            excError=ReadExcelData().returnExcelData('data.xlsx', 'login',9,3)
            self.assertEqual(error,excError)
            mylogger.debug("test08执行结果：成功")
        except Exception as e:
            mylogger.debug("test08执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test08")
     def test09(self):
        mylogger.debug("执行用例：密码输入21位")
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',10,2)
        password2=ReadExcelData().returnExcelData('data.xlsx', 'login',10,3)
        LoginPage().click_password().send_keys(password)
        time.sleep(2)
        try:
            password1=self.driver.find_elements_by_tag_name('input')[1].get_attribute('value')
            self.assertEqual(password1,password2)
            mylogger.debug("test09执行结果：成功")
        except Exception as e:
            mylogger.debug("test09执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test09")

     def test10(self):
        mylogger.debug("执行用例：密码输入20位")
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',11,2)
        password2=ReadExcelData().returnExcelData('data.xlsx', 'login',11,3)
        LoginPage().click_password().send_keys(password)
        time.sleep(2)
        try:
            password1=self.driver.find_elements_by_tag_name('input')[1].get_attribute('value')
            self.assertEqual(password1,password2)
            mylogger.debug("test10执行结果：成功")
        except Exception as e:
            mylogger.debug("test10执行结果：失败")
            mylogger.debug(e)
            CommonDef().get_windows_img("img_test10")


     def test11(self):
        mylogger.debug("执行用例：用户名正确，密码正确")
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'login',1,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'login',1,2)
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)
        #判断是否登录成功
        try:
            username2 = self.driver.find_element_by_partial_link_text(username).text
            self.assertEqual(username2,username,"登录成功")
            mylogger.debug("test11执行结果：成功")
        except Exception as e:
            #CommonDef().get_windows_img("img_test11")
            CommonDef().get_windows_img("img_test11")
            mylogger.debug("test11执行结果：失败")
            mylogger.debug(e)











