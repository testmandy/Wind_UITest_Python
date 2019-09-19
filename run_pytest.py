# coding=utf-8
# @Time    : 2019/9/3 9:47
# @Author  : Mandy
import configparser
import os
import sys

import conftest
from common import Utility_Android


def delete_log():
    """
    定义方法：创建文件夹，并清除垃圾文件
    """
    make_and_clean_folder('output')
    make_and_clean_folder('report')
    make_and_clean_folder('testapp')
    make_and_clean_folder('screenshots')
    make_and_clean_folder('allure-report')


def make_and_clean_folder(folder_name):
    """
    定义方法：创建文件夹，并清除垃圾文件
    """
    if not os.path.exists(folder_name):
        os.system(r'mkdir ' + folder_name)
    new_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)
    # 删除文件夹下的文件
    os.system(r'del /s/q ' + new_dir)


def modify_env_config(section, key, value):
    config_env_file = conftest.env_dir
    cp = configparser.ConfigParser()
    cp.read(config_env_file, encoding="UTF-8")
    cp.set(section, key, value)


def stop_server():
    os.system(r'tskill node')


def run_case(mark, platform):
    case_path = None
    result_path = conftest.report_dir
    if platform == 'android':
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    command = os.system(r'pytest -v -s -m "%s" %s --alluredir %s' % (mark, case_path, result_path))
    print(command)


def install_and_run_case(mark, platform):
    case_path = None
    result_path = conftest.report_dir
    if platform == 'android':
        modify_env_config('caps', 'noReset_flag', 'false')
        # 远程下载apk包
        Utility_Android.download_and_move()
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    command = os.system(r'pytest -v -s -m "%s" %s %s ' % (mark, case_path, result_path))
    print(command)


def main(modules, install_flag, telephone, platform):
    delete_log()
    modify_env_config('Common', 'telephone', telephone)
    modules_str = modules.replace(',', ' or ')
    if install_flag is 'yes':
        install_and_run_case(modules_str, platform)
    else:
        run_case(modules_str, platform)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        modules = 'mine'
        install_flag = 'yes'
        telephone = '15212345678'
        platform = 'android'
        main(modules, install_flag, telephone, platform)
    else:
        modules = sys.argv[1]
        install_flag = sys.argv[2]
        telephone = sys.argv[3]
        platform = sys.argv[4]
        main(modules, install_flag, telephone, platform)



