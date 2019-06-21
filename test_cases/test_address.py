# -*- coding:utf-8 -*-

from common_method.common_def import CommonDef
from pages.address_page import AddressPage
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.member_center import MemberCenter
from utils.get_selenium_driver import GetSeleniumDriver
from utils.logger import Logger
from utils.mysql_connection import MysqlConnection
from utils.read_excel_data import ReadExcelData

#from utils.create_connection_mysql import CreateConnectionMysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import unittest,time
mylogger = Logger(__name__).getlog()
class TestAddress(unittest.TestCase):
    #继承unnittest初始化方法
    @classmethod
    def setUpClass(cls):
        cls.driver = GetSeleniumDriver().driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver = GetSeleniumDriver().driver
        url=ReadExcelData().returnExcelData('data.xlsx', 'index', 0,1)
        self.driver.get(url)
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        #点击请登录
        IndexPage().click_login_link().click()
        #输入用户名
        username=ReadExcelData().returnExcelData('data.xlsx', 'index',2,1)
        LoginPage().click_username().send_keys(username)
        #输入密码
        password=ReadExcelData().returnExcelData('data.xlsx', 'index',3,1)
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        #判断是否登录成功
        '''
        def is_login_sucess(cls):
           #判断是否获取到登录账户名称
           try:
                text = cls.driver.find_element_by_id("lnk_current_user").text
                print text
                return True
            except:
                return False
        '''
        #获取当前窗口句柄
        nowhandle=self.driver.current_window_handle
        time.sleep(2)
        #点击首页-会员中心
        IndexPage().click_member_center().click()
        mylogger.debug("点击首页-会员中心")
        self.driver.implicitly_wait(5)
        #获取所有handle
        allhandles=self.driver.window_handles
        #循环，当句柄不等于首页句柄时，转换为现在的窗口句柄
        for handle in allhandles:
            if handle!=nowhandle:
                self.driver.switch_to_window(handle)
        time.sleep(2)
        #点击会员中心-收货地址
        MemberCenter().clink_address_link().click()
        mylogger.debug("点击会员中心-收货地址")
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.delete_all_cookies()
#编辑收货地址
    def test01(self):
        mylogger.debug("开始编辑地址")
        #点击编辑
        mylogger.debug("点击编辑")
        try:
            AddressPage().click_edit_address().click()
        except Exception:
            assert False,"未能成功点击编辑按钮"
        self.driver.implicitly_wait(5)
        #清空收货人原有内容
        mylogger.debug("清空收货人原有内容")
        AddressPage().input_edit_name_id().clear()
        try:
            AddressPage().input_edit_name_id().clear()
        except Exception:
            assert False,"未能成功清空收货人原有信息"
        time.sleep(4)
        #编辑收货人
        mylogger.debug("编辑收货人")
        try:
            edit_name=ReadExcelData().returnExcelData('data.xlsx', 'address',0,1)
            AddressPage().input_edit_name_id().send_keys(edit_name)
        except Exception:
            assert False,"未能成功编辑收货人"
        self.driver.implicitly_wait(5)
        #选择地址_省
        mylogger.debug("选择地址_省")
        try:
            AddressPage().select_edit_province_id().click()
        except Exception:
            assert False,"未能成功选择地址_省"
        time.sleep(2)
        #选择地址_市
        mylogger.debug("选择地址_市")
        try:
            AddressPage().select_edit_city_id().click()
        except Exception:
            assert False,"未能成功选择地址_省"
        time.sleep(2)
        #选择地址_区
        mylogger.debug("选择地址_区")
        try:
            AddressPage().select_edit_county_id().click()
        except Exception:
            assert False,"未能成功选择地址_区"
        time.sleep(2)
        #清空详细地址原有内容
        mylogger.debug("清空详细地址原有内容")
        try:
            AddressPage().input_edit_detailaddress_id().clear()
        except Exception:
            assert False,"未能成功清空详细地址原有内容"
        #编辑详细地址
        mylogger.debug("编辑详细地址")
        try:
            edit_address=ReadExcelData().returnExcelData('data.xlsx', 'address',1,1)
            AddressPage().input_edit_detailaddress_id().send_keys(edit_address)
        except Exception:
            assert False,"未能成功编辑详细地址"
        self.driver.implicitly_wait(5)
        #清空手机号原有内容
        mylogger.debug("清空手机号原有内容")
        try:
            AddressPage().input_edit_mobile_id().clear()
        except Exception:
            assert False,"未能成功清空手机号原有内容"
        #编辑手机号
        mylogger.debug("编辑手机号")
        try:
            edit_mobile=ReadExcelData().returnExcelData('data.xlsx', 'address',2,1)
            AddressPage().input_edit_mobile_id().send_keys(str(edit_mobile))
        except Exception:
            assert False,"未能成功编辑手机号"
        time.sleep(5)
        #截屏
        CommonDef().get_windows_img()
        #点击保存收货地址
        mylogger.debug("点击保存收货地址")
        # JavascriptExecutor executor = (JavascriptExecutor) driver;
        # executor.executeScript("arguments[0].click();",AddressPage().click_edit_button());
        try:
            AddressPage().click_edit_button().click()
        except Exception:
            assert False,"未能成功点击确认修改按钮"
        time.sleep(2)
        #截屏
        CommonDef().get_windows_img()
        time.sleep(2)
#新增收货地址
    def test02(self):
        mysql_host=ReadExcelData().returnExcelData('data.xlsx', 'mysql',0,1)
        mysql_user=ReadExcelData().returnExcelData('data.xlsx', 'mysql',1,1)
        mysql_password=ReadExcelData().returnExcelData('data.xlsx', 'mysql',2,1)
        mysql_port=ReadExcelData().returnExcelData('data.xlsx', 'mysql',3,1)
        mysql_database=ReadExcelData().returnExcelData('data.xlsx', 'mysql',4,1)
        _sql1=ReadExcelData().returnExcelData('data.xlsx', 'mysql',6,1)
        _sql2=ReadExcelData().returnExcelData('data.xlsx', 'mysql',7,1)
        count=MysqlConnection().count_mysql(mysql_host,int(mysql_port),mysql_user,mysql_password,mysql_database,"utf8",_sql1)
        print count[0]
        time.sleep(3)
        if count[0]==10:
            MysqlConnection().del_mysql(mysql_host,int(mysql_port),mysql_user,mysql_password,mysql_database,"utf8",_sql2)
        else:
            pass
        time.sleep(3)
        count=MysqlConnection().count_mysql(mysql_host,int(mysql_port),mysql_user,mysql_password,mysql_database,"utf8",_sql1)
        print count[0]
        mylogger.debug("开始新增地址")
        #点击新增
        AddressPage().click_add_address_class().click()
        time.sleep(3)
        #输入收货人
        add_name=ReadExcelData().returnExcelData('data.xlsx', 'address',3,1)
        AddressPage().click_add_name().send_keys(add_name)
        self.driver.implicitly_wait(5)
        mylogger.debug("输入收货人")
        #选择省
        AddressPage().click_add_province().click()
        time.sleep(2)
        mylogger.debug("选择省")
        #选择市
        AddressPage().click_add_city().click()
        time.sleep(2)
        mylogger.debug("选择市")
        #选择区
        AddressPage().click_add_county().click()
        time.sleep(2)
        mylogger.debug("选择区")
        #S输入详细地址
        add_address=ReadExcelData().returnExcelData('data.xlsx', 'address',4,1)
        AddressPage().click_add_detailaddress().send_keys(add_address)
        self.driver.implicitly_wait(5)
        mylogger.debug("输入详细地址")
        #输入手机号
        add_mobile=ReadExcelData().returnExcelData('data.xlsx', 'address',5,1)
        AddressPage().click_add_mobile().send_keys(str(add_mobile))
        self.driver.implicitly_wait(5)
        self.driver.implicitly_wait(5)
        mylogger.debug("输入手机号")
        #点击提交按钮
        AddressPage().click_add_button().click()
        self.driver.implicitly_wait(5)
        mylogger.debug("点击提交按钮")
        #截屏
        CommonDef().get_windows_img()
        # CreateConnectionMysql().connection_mysql(mysql_host,int(mysql_port),mysql_user,mysql_password,mysql_database,"utf8")
        # CreateConnectionMysql().cureors() #数据库游标
        _sql=ReadExcelData().returnExcelData('data.xlsx', 'mysql',5,1)
        MysqlConnection().connection_mysql(mysql_host,int(mysql_port),mysql_user,mysql_password,mysql_database,"utf8",_sql)
        # CreateConnectionMysql().selects(_sql)
        # CreateConnectionMysql().closes()

if __name__ == '__main__':
    unittest.main()


