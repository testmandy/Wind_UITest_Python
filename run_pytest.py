# coding=utf-8
# @Time    : 2019/9/3 9:47
# @Author  : Mandy
import os
import sys

import conftest
from utils.server import Server


def run_case(platform, start_server_flag='yes'):
    case_path = None
    if platform == 'android':
        case_path = conftest.android_case_dir
    elif platform == 'ios':
        case_path = conftest.ios_case_dir
    if start_server_flag == 'yes':
        start_server = Server()
        start_server.main(platform)
    os.system(r'pytest -v -s -m %s --alluredir ./allure_result/' % case_path)

def main(platform):
    run_case(platform)


if __name__ == '__main__':
    """
    python run.py $App $System $Source $Model $Priority $Rerunfailedcase $Install android $Concurrency
        if len(sys.argv) != 10:
        sys.exit()
    app = sys.argv[1]
    system = sys.argv[2]
    app_download_path = sys.argv[3]
    model = sys.argv[4].split(',')
    priority = sys.argv[5].split(',')
    rerun_failedcase = sys.argv[6]
    install_flag = sys.argv[7]
    platform = sys.argv[8]
    concurrency = sys.argv[9]
    main(app,system,app_download_path,model,priority,rerun_failedcase,install_flag,platform,concurrency)
    """
    platform = sys.argv[1]
    main(platform)




