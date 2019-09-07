# coding=utf-8
# @Time    : 2019/9/3 9:47
# @Author  : Mandy
import configparser
import os
import sys
import conftest
from common import Utility_Android
from common.base_driver import BaseDriver
from utils.server import Server


def delete_log():
    """
    定义方法：创建文件夹，并清除垃圾文件
    """
    if not os.path.exists('output'):
        os.system(r'mkdir output')
    if not os.path.exists('report'):
        os.system(r'mkdir report')
    if not os.path.exists('testapp'):
        os.system(r'mkdir testapp')
    if not os.path.exists('screenshots'):
        os.system(r'mkdir screenshots')
    if not os.path.exists('allure_result'):
        os.system(r'mkdir allure_result')

    os.system(r'rm -f ./output/*.*')
    os.system(r'touch ./output/log.log')
    os.system(r'rm -f ./report/*.*')
    os.system(r'rm -f ./testapp/*.*')
    os.system(r'rm -f ./screenshots/*.*')
    os.system(r'rm -f ./allure_result/*.*')


def modify_env_config(noReset_flag_android, platform):
    config_env_file = conftest.env_dir
    cp = configparser.ConfigParser()
    cp.read(config_env_file, encoding="UTF-8")
    cp.set('caps', 'noReset_flag', noReset_flag_android)
    if platform == 'android':
        # 远程下载apk包
        Utility_Android.download_and_move()

def stop_server():
    os.system(r'tskill node')


def run_case(mark, platform):
    case_path = None
    if platform == 'android':
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    command = os.system(r'pytest -v -s -m "%s" %s ' % (mark, case_path))
    print(command)


def install_and_run_case(mark, platform):
    case_path = None
    if platform == 'android':
        modify_env_config(False, 'android')
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    command = os.system(r'pytest -v -s -m "%s" %s ' % (mark, case_path))
    print(command)


def main(modules, install_flag, platform):
    delete_log()
    modules_str = modules.replace(',', ' or ')
    if install_flag is 'yes':
        install_and_run_case(modules_str, platform)
    else:
        run_case(modules_str, platform)


if __name__ == '__main__':
    """
    python run.py $App $System $Source $Model $Priority $Rerunfailedcase $Install android $Concurrency
        if len(sys.argv) != 10:
        sys.exit()
    main(app,system,app_download_path,model,priority,rerun_failedcase,install_flag,platform,concurrency)
    """
    modules = sys.argv[1]
    install_flag = sys.argv[2]
    platform = sys.argv[3]
    # modules = 'common'
    # install_flag = 'no'
    # platform = 'android'
    main(modules, install_flag, platform)




