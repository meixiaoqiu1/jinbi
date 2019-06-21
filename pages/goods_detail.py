#-*-coding:utf-8-*-
from utils.get_selenium_driver import GetSeleniumDriver
import time
class RES():
    buy_id="detailBuy"#立即购买
class GoodsDetail(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    def click_buy_id(self):
        try:
            click_buy_id=self.driver.find_element_by_id(RES().buy_id)
            return click_buy_id
        except Exception:
            assert False,"未能成功点击立即购买"
    time.sleep(2)