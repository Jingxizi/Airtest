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


import logging
# ，这样INFO和DEBUG级别的日志就不会显示在控制台
logging.getLogger("airtest").setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)


# 禁用paddlepaddle的DEBUG信息
os.environ['GLOG_minloglevel'] = '2'

# 设置整体日志级别
logging.basicConfig(level=logging.ERROR)



# using("/Users/cczq/software/iOS_Proj/Airtest/test2.air")

# from test2 import ttt
# ttt()



touch(Template(r"tpl1755676707653.png", record_pos=(-0.196, 0.946), resolution=(1178, 2556)))








