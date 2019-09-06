# coding=utf-8
# @Time    : 2019/9/3 9:47
# @Author  : Mandy
import os
import sys
import conftest
from common.base_driver import BaseDriver
from utils.server import Server


def stop_server():
    os.system(r'tskill node')


def run_case(mark, platform, start_server_flag='yes'):
    case_path = None
    if platform == 'android':
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    # if start_server_flag == 'yes':
    #     start_server = Server()
    #     start_server.main(platform)
    command = os.system(r'pytest -v -s -m "%s" %s ' % (mark, case_path))
    print(command)


def main(modules, platform):
    modules_str = modules.replace(',', ' or ')
    run_case(modules_str, platform)


if __name__ == '__main__':
    """
    python run.py $App $System $Source $Model $Priority $Rerunfailedcase $Install android $Concurrency
        if len(sys.argv) != 10:
        sys.exit()
    main(app,system,app_download_path,model,priority,rerun_failedcase,install_flag,platform,concurrency)
    """
    modules = sys.argv[1]
    platform = sys.argv[2]
    main(modules, platform)




