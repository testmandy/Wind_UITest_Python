# coding=utf-8
# @Time    : 2019/9/3 9:47
# @Author  : Mandy
import os

import conftest

if __name__ == '__main__':
    os.system("pytest " + conftest.android_case_dir)

