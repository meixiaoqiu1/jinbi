#-*-coding:utf-8-*-
from utils.get_selenium_driver import  GetSeleniumDriver
import time

class RES():
    username_id="js_username" #用户名
    passwords_id="js_password"#密码
    login_submit_button_id="js_submit"#登录按钮
    code_id="js_code_img"#验证码
class LoginPage(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    def click_username(self):#定位到用户名
        try:
            click_username=self.driver.find_element_by_id(RES.username_id)
            return click_username
        except Exception:
            assert False,"未定位到用户名"



    def click_password(self):
        try:
            click_password=self.driver.find_element_by_id(RES.passwords_id)
            return click_password
        except Exception:
            assert False,"未定位到密码框"


    def click_password(self):
        try:
            click_password=self.driver.find_element_by_id(RES.passwords_id)
            return click_password
        except Exception:
            assert False,"未定位到密码框"

    def input_code(self):
        try:
            click_code=self.driver.find_element_by_id(RES.code_id)
            return click_code

        except Exception:
            assert False,"未定位到验证码"

    def click_login_submit(self):
        try:
            click_login_submmit=self.driver.find_element_by_id(RES.login_submit_button_id)
            return click_login_submmit
        except Exception:
            assert False,"未定位到登录按钮"


