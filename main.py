from airtest.cli.runner import run_script
from argparse import Namespace

args = Namespace(
    script="/Users/cczq/software/iOS_Proj/Airtest/test1.air",
    device=["ios:///http://172.23.1.200:8100"],
    log="/Users/cczq/software/iOS_Proj/Common/log/airtest",
    recording=None, # 是否录屏
    compress=None,	# 截图质量
    no_image=None 	# 是否跳过截图
)

run_script(args)




























