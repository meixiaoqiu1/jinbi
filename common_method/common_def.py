#-*-coding:utf-8-*-
from utils.get_selenium_driver import GetSeleniumDriver
from pages.index_page import IndexPage
from pages.login_page import LoginPage
import time
import os
from PIL import Image
import pytesseract
from PIL import ImageEnhance
from utils.logger import Logger
mylogger = Logger(__name__).getlog()

class CommonDef(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    #滚动条下滑
    def huadong_gundongtiao(self):
        js1="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
        time.sleep(2)

    def huadong_gundoongtiao2(self,a):
        target =a
        self.driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去

    # def jubing(self):
    ##获取当前窗口句柄
    # nowhandle=self.driver.current_window_handle
    ##获取所有handle
    #allhandles=self.driver.window_handles
    #     #循环，当句柄不等于首页句柄时，转换为现在的窗口句柄
    #     for handle in allhandles:
    #         if handle!=nowhandle:
    #             self.driver.switch_to_window(handle)

    # 保存图片
    def get_windows_img(self,img_name):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/picture/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + img_name+rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylogger.debug("Had take screenshot and save to folder : /picture")
        except NameError as e:
            mylogger.debug("Failed to take screenshot! %s" % e)
            self.get_windows_img(screen_name)
    # # 保存图片
    # def get_windows_img(self):
    #     """
    #     在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
    #     """
    #     file_path = os.path.dirname(os.path.abspath('.')) + '/picture/'
    #     rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    #     screen_name = file_path + rq + '.png'
    #     try:
    #         self.driver.get_screenshot_as_file(screen_name)
    #         mylogger.debug("Had take screenshot and save to folder : /picture")
    #     except NameError as e:
    #         mylogger.debug("Failed to take screenshot! %s" % e)
    #         self.get_windows_img()

    def login(self,url,username,password):
        #self.driver = GetSeleniumDriver().driver
        self.driver.get(url)
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        #点击请登录
        IndexPage().click_login_link().click()
        time.sleep(1)
        #输入用户名
        LoginPage().click_username().send_keys(username)
        time.sleep(1)
        #输入密码
        LoginPage().click_password().send_keys(password)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(1)
        #输入验证码
        #获取截图
        # dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # image_path=os.path.join(dir_path,'picture\screenshot.png')
        # self.driver.get_screenshot_as_file(image_path)
        #
        # #获取指定元素位置
        # element = self.driver.find_element_by_id('js_code_img')
        # left = int(element.location['x'])
        # top = int(element.location['y'])
        # right = int(element.location['x'] + element.size['width'])
        # bottom = int(element.location['y'] + element.size['height'])
        #
        # #通过Image处理图像
        # im = Image.open(image_path)
        # im = im.crop((left, top, right, bottom))
        # code_path=os.path.join(dir_path,'picture\code.png')
        # im.save(code_path)
        # image=Image.open(code_path)
        # image = image.convert('L') #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        # sharpness =ImageEnhance.Contrast(image)#对比度增强
        # image = sharpness.enhance(3.0) #3.0为图像的饱和度
        # image.show()
        # vcode=pytesseract.image_to_string(image)
        # time.sleep(1)
        # print vcode
        # time.sleep(1)
        # #输入验证码
        # LoginPage().input_code().send_keys(vcode.strip())
        #
        # time.sleep(3)
        # #点击登录按钮
        # LoginPage().click_login_submit().click()
        # time.sleep(3)

    def quit(self):
        self.driver.quit()