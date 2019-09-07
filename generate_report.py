# coding=utf-8
# @Time    : 2019/9/7 19:01
# @Author  : Mandy

import os

# 生成html报告
import conftest

command = os.system('allure generate report --clean')
print(command)
allure_report_path = os.path.join(conftest.project_dir, '\\allure-report\\index.html')
print("Please visit the report file at: " + '\n' + allure_report_path)
