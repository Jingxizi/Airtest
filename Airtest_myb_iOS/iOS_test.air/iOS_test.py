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



test_account = "1001990"
test_password = "111111"

print("▊▊▊test_start")
# 

# sw sh 屏幕宽度 高度
sw, sh = device().get_current_resolution()
print(f"▊▊▊设备宽高{sw}, {sh}")










touch(Template(r"tpl1739324163466.png", record_pos=(-0.115, -0.554), resolution=(1178, 2556)))


while not exists(Template(r"tpl1739341705670.png", record_pos=(0.012, -0.742), resolution=(1178, 2556))) and not exists(Template(r"tpl1739324505783.png", record_pos=(-0.001, -0.697), resolution=(1178, 2556))):
    print("▊▊▊等待加载至宣传页")
    time.sleep(1)

print("▊▊▊已加载至宣传页")

if exists(Template(r"tpl1739324505783.png", record_pos=(-0.001, -0.697), resolution=(1178, 2556))):
    touch(Template(r"tpl1739324524162.png", record_pos=(0.188, 0.704), resolution=(1178, 2556)))

time.sleep(2)

print("▊▊▊滑动跳过宣传页")
for i in range(3):
    swipe((0.8*sw,0.8*sh),(0.3*sw,0.8*sh),duration=0.5) 
time.sleep(1)
print("▊▊▊滑动结束") 

if exists(Template(r"tpl1739341490692.png", record_pos=(-0.003, 0.761), resolution=(1178, 2556))):
    touch(Template(r"tpl1739341512414.png", record_pos=(-0.004, 0.761), resolution=(1178, 2556)))

while not exists(Template(r"tpl1739342186640.png", record_pos=(-0.402, 0.941), resolution=(1178, 2556))) and not exists(Template(r"tpl1739324215791.png", record_pos=(-0.003, -0.459), resolution=(1178, 2556))):
    print("▊▊▊等待加载至首页")
    time.sleep(1)    
    
if exists(Template(r"tpl1739324215791.png", record_pos=(-0.003, -0.459), resolution=(1178, 2556))):
    touch(Template(r"tpl1739324225344.png", record_pos=(-0.006, 0.457), resolution=(1178, 2556)))
    time.sleep(1)

    
    
    
def getCaptcha():
    sw, sh = device().get_current_resolution()

    # 截图验证码
    screen = G.DEVICE.snapshot()
    screen = aircv.crop_image(screen,(int(0.8*sw),int(0.32*sh),int(0.985*sw),int(0.365*sh)))

    SavePath = './'
    filename = 'login_captcha.jpg'
    filepath = os.path.join(SavePath, filename)
    aircv.imwrite(filepath, screen, 99) 
    
    
    ocr_count=10
    result_captcha=None
    while ocr_count > 0:
        result = ocr.ocr(filepath, det=False, cls=False)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(f"▊▊▊line{line}")
                orinum = line[0]
                orinum = orinum.replace(" ", "")
                orinum = orinum.replace("　", "")
                print(f"▊▊▊识别结果{orinum}")
                if orinum.isdigit() and len(orinum) == 4:
                    result_captcha = orinum
                    break
            if result_captcha:
                break
        if result_captcha:
            break
        else:
            ocr_count -= 1
            print(f"▊▊▊ OCR未识别到有效验证码，剩余尝试次数: {ocr_count}")
    
    if result_captcha:
        print(f"▊▊▊验证码识别成功: {result_captcha}")
    else:
        print("▊▊▊验证码识别失败")
        
    return result_captcha

    

    
    



def login(account, password):
    if exists(Template(r"tpl1739343643294.png", record_pos=(-0.213, -0.593), resolution=(1178, 2556))) and exists(Template(r"tpl1739343743964.png", record_pos=(-0.007, 0.222), resolution=(1178, 2556))):
        print("▊▊▊已进入登录页")
    else:
        print("▊▊▊未进入登录页")
        return False
    
    captcha = getCaptcha()
    print(f"▊▊▊captcha{captcha}")
    
    touch(Template(r"tpl1739343643294.png", record_pos=(-0.213, -0.593), resolution=(1178, 2556)))
    time.sleep(2)
    text(account)
    touch(Template(r"tpl1739344439206.png", record_pos=(-0.219, -0.468), resolution=(1178, 2556)))
    time.sleep(2)
    text(password)
    
    touch(Template(r"tpl1739344456221.png", record_pos=(-0.238, -0.222), resolution=(1178, 2556)))
    time.sleep(2)
    text(captcha)

    
    

login(test_account, test_password)

touch(Template(r"tpl1739430510050.png", record_pos=(0.0, -0.474), resolution=(1178, 2556)))
touch(Template(r"tpl1739430521194.png", record_pos=(-0.194, 0.492), resolution=(1178, 2556)))
touch(Template(r"tpl1739430533995.png", record_pos=(-0.003, -0.135), resolution=(1178, 2556)))

touch(Template(r"tpl1739430542127.png", record_pos=(-0.003, 0.214), resolution=(1178, 2556)))
touch(Template(r"tpl1739430567644.png", record_pos=(-0.109, -0.017), resolution=(1178, 2556)))
touch(Template(r"tpl1739430574288.png", record_pos=(-0.172, 0.154), resolution=(1178, 2556)))
touch(Template(r"tpl1739430597376.png", record_pos=(-0.245, -0.247), resolution=(1178, 2556)))
touch(Template(r"tpl1739430601879.png", record_pos=(-0.002, -0.357), resolution=(1178, 2556)))
touch(Template(r"tpl1739430608644.png", record_pos=(-0.006, 0.351), resolution=(1178, 2556)))











