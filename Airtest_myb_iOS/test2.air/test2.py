# -*- encoding=utf8 -*-
__author__ = "cczq"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.ios import iosPoco
poco = iosPoco()

import time

from airtest.aircv import *


from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en') 


# connect_device("android://127.0.0.1:5037/emulator-5554")


import logging


# 将airtest日志记录器的级别设置为ERROR，这样INFO和DEBUG级别的日志就不会显示在控制台
logging.getLogger("airtest").setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)


# 禁用paddlepaddle的DEBUG信息
os.environ['GLOG_minloglevel'] = '2'

# 设置整体日志级别
logging.basicConfig(level=logging.ERROR)



def ttt():
    touch(Template(r"tpl1755676718219.png", record_pos=(-0.005, 0.943), resolution=(1178, 2556)))



ttt()




