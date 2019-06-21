#-*-coding:utf-8-*-
from utils.get_selenium_driver import  GetSeleniumDriver
import time
class RES():
    question_id="questionCodeText"#问题框
    order_submit_button_id="btnSumit"#提交订单按钮
class OrderSubmitPage(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    def input_question_id(self):
        try:
            input_question_id=self.driver.find_element_by_id(RES.question_id)
            return input_question_id
        except Exception:
            assert False,"未定位到问题框"
        time.sleep(2)
    def click_order_submit(self):
        try:
            click_order_submit=self.driver.find_element_by_id(RES.order_submit_button_id)
            return click_order_submit
        except Exception:
            assert False,"未能成功点击提交订单按钮"
        time.sleep(2)