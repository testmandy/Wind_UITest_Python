# coding=utf-8
# @Time    : 2019/9/7 19:01
# @Author  : Mandy

import os

# # 生成html报告
import conftest

command = os.system('allure generate report --clean')
print(command)

