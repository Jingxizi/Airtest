from airtest.cli.runner import run_script
from argparse import Namespace



common_args = {
    "device": ["ios:///http://172.23.1.200:8100"],
    "log": "/Users/cczq/software/iOS_Proj/Common/log/airtest",
    "recording": None,
    "compress": None,
    "no_image": None
}

args1 = Namespace(script="/Users/cczq/software/iOS_Proj/Airtest/test1.air", **common_args)
args2 = Namespace(script="/Users/cczq/software/iOS_Proj/Airtest/test2.air", **common_args)


run_script(args1)
run_script(args2)


























