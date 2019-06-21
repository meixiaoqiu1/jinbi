#-*-coding:utf-8-*-
from utils.get_selenium_driver import GetSeleniumDriver
from utils.logger import Logger
mylogger = Logger(__name__).getlog()
import time
class RES():
    ############################################# 收货地址 #########################################################
    add_address_class="anniu"#这里的class是“anniu marl10”，中间有空格，我们在编写自动化的时候可以用.代替或者只写前部分
    #add_address_class="anniu.marl10"
    edit_adress_link="编辑"
    #editd_address_xpath="//*[@id='viewAddressList1']/ul/li[1]/a"
    ############################################# 编辑收货地址框 #######################################################
    edit_name_id="consignee1"  #收货人
    edit_province_id="city_1_0" #收货地址中的省
    edit_city_id="city_1_1"  #收货地址中的市
    edit_county_id="city_1_2" #收货人中的县
    edit_detailaddress_id="detailsAddress1"#详细地址
    edit_mobile_id="mobile1"#手机号码
    #edit_button_class="in_btn"#确认修改按钮
    #edit_button_xpath="//*[@id='viewAddress1']/td/table/tbody/tr[9]/td[2]/input"
    edit_button_link="确认修改"
    ############################################# 新增收货地址框 #######################################################
    add_name_id="consignee"#新增收货人
    add_province_id="city__0"#收货地址中的省
    add_city_id="city__1"  #收货地址中的市
    add_county_id="city__2" #收货人中的县
    add_detailaddress_id="detailsAddress"#详细地址
    add_mobile_id="mobile"#手机号码
    add_button_id="saveNewAddressBtn"
class AddressPage(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver

    ############################################# 编辑收货地址框 #######################################################
    #点击编辑
    def click_edit_address(self):
            click_edit_address=self.driver.find_element_by_link_text(RES.edit_address_link)
            return click_edit_address
    #编辑收货人
    def input_edit_name_id(self):
            input_edit_name_id=self.driver.find_element_by_id(RES.edit_name_id)
            return input_edit_name_id
    #编辑省
    def select_edit_province_id(self):
            select_edit_province_id=self.driver.find_element_by_id(RES.edit_province_id).find_element_by_xpath("//option[@value='002004']")
            return select_edit_province_id
    #选择市
    def select_edit_city_id(self):
            select_edit_city_id=self.driver.find_element_by_id(RES.edit_city_id).find_element_by_xpath("//option[@value='002004002']")
            return select_edit_city_id
    #选择区
    def select_edit_county_id(self):
            select_edit_county_id=self.driver.find_element_by_id(RES.edit_county_id).find_element_by_xpath("//option[@value='002004002008']")
            return select_edit_county_id
    #定位详细地址
    def input_edit_detailaddress_id(self):
            input_edit_detailaddress_id=self.driver.find_element_by_id(RES.edit_detailaddress_id)
            return input_edit_detailaddress_id

    def input_edit_mobile_id(self):
            input_edit_mobile_id=self.driver.find_element_by_id(RES.edit_mobile_id)
            return input_edit_mobile_id
    #定位手机号
    def click_edit_button(self):
            #click_edit_button=self.driver.find_element_by_xpath("//*[@id='viewAddress1']/td/table/tbody/tr[9]/td[2]/input")
            #click_edit_button=self.driver.find_element_by_xpath("/html/body/div[10]/div/form/div/div[2]/table/tbody").find_element_by_xpath(RES.edit_button_xpath)
            #click_edit_button=self.driver.find_element_by_xpath("/html/body/div[10]/div/form/div/div[2]/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input")
            #click_edit_button=self.driver.find_element_by_id("viewAddress1").find_element_by_css_selector("[onclick='memberAddressSave('1','2');']")
            click_edit_button=self.driver.find_element_by_link(RES.edit_button_link )
            return click_edit_button

    ############################################# 新增收货地址框 #######################################################
    def click_add_address_class(self):
            click_add_address=self.driver.find_element_by_class_name(RES.add_address_class)
            return click_add_address

    def click_add_address(self):
            click_add_address=self.driver.find_element_by_class_name(RES.add_address_class)
            return click_add_address

    def click_add_name(self):
            click_add_name=self.driver.find_element_by_id(RES.add_name_id)
            return click_add_name

    def click_add_province(self):
            click_add_province=self.driver.find_element_by_id(RES.add_province_id).find_element_by_xpath("//option[@value='002004']")
            return click_add_province

    def click_add_city(self):
            click_add_city=self.driver.find_element_by_id(RES.add_city_id).find_element_by_xpath("//option[@value='002004002']")
            return click_add_city

    def click_add_county(self):
            click_add_county=self.driver.find_element_by_id(RES.add_county_id).find_element_by_xpath("//option[@value='002004002008']")
            return click_add_county

    def click_add_detailaddress(self):
            click_add_detailaddress=self.driver.find_element_by_id(RES.add_detailaddress_id)
            return click_add_detailaddress

    def click_add_mobile(self):
            click_add_mobile=self.driver.find_element_by_id(RES.add_mobile_id)
            return click_add_mobile

    def click_add_button(self):
            click_add_button=self.driver.find_element_by_id(RES.add_button_id)
            return click_add_button

