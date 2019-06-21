#!/usr/bin/env python
# -*- coding: UTF-8 -*

###############################   FanFandata   ################################
# version:      0.0.1
# filename:     Logger.py
# description： Log日志方法封装
###############################################################################
import os
import sys
import time

import logging
import logging.handlers

#os.path.abspath(path) 返回path规范化的绝对路径。os.pardir是指的os模块中的pardir这个对象，在window中这个代表着上级目录
#os.path模块http://www.cnblogs.com/wuxie1989/p/5623435.html
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(ROOT_DIR)

class Logger():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def __init__(self, name=None):
        # 定义日志存放路径
        self.path = os.path.join(ROOT_DIR, 'log_reports/Log')
        rq = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # 日志文件名称
        self.filename = self.path + rq + '.log'
        # 为%(name)s赋值
        if name is None:
            self.logger = logging.getLogger('logger')
            #控制日志文件中记录级别
            self.logger.setLevel(logging.DEBUG)
            #控制输出到控制台日志格式、级别
            self.ch = logging.StreamHandler()
            gs = logging.Formatter('%(asctime)s - %(levelname)s -  %(module)s[line:%(lineno)d] - %(message)s')
            self.ch.setFormatter(gs)
        else:
            self.logger = logging.getLogger(name)
            #控制日志文件中记录级别
            self.logger.setLevel(logging.DEBUG)
            #控制输出到控制台日志格式、级别
            self.ch = logging.StreamHandler()
            gs = logging.Formatter('%(asctime)s - %(levelname)s -  %(name)s[line:%(lineno)d] - %(message)s')
            self.ch.setFormatter(gs)
        # self.ch.setLevel(logging.NOTSET)
        #创建一个handler，用于写入日志文件 (每天生成1个，保留10天的日志)
        self.fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 10)
        self.fh.suffix = "%Y%m%d-%H%M.log"
        self.fh.setLevel(logging.DEBUG)

        #定义日志文件中格式
        self.fh.setFormatter(gs)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def getlog(self):
        return self.logger