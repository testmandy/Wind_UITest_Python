# coding=utf-8
# @Time    : 2019/9/6 14:38
# @Author  : Mandy
import os
from datetime import datetime

import requests

import conftest
from common.read_ini import ReadIni


def download_apk(num, url):
    """
    下载文件
    :param url:下载链接
    :param num:索引值
    """
    global count
    count = 0
    succeed = 'Succeed'
    failure = 'Failure'
    print('第' + str(num) + '条url:\n' + url)
    filename = os.path.basename(url)
    filename = filename.split('?')[0]
    response = requests.head(url)
    filesize = round(float(response.headers['Content-Length']) / 1048576, 2)
    apk_format = 'application/vnd.android.package-archive'

    # 过滤非zip文件或大于100.00M的文件
    # TODO 可按需修改
    if response.headers['Content-Type'] == apk_format and filesize < 100.00:
        print('文件类型：' + response.headers['Content-Type'] + "\n" +
              '文件大小：' + str(filesize) + 'M' + "\n" +
              '文件名：' + str(filename))

        # 下载文件
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) '
                          'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Connection': 'keep-alive', }
        file = requests.get(url, headers=headers, timeout=10)

        with open(filename, 'wb') as apk:
            apk.write(file.content)
            print(succeed + "\n")
            count += 1

        # 返回内容
        dicts = [url, succeed, filename]
        return dicts
    else:
        print('文件类型:' + response.headers['Content-Type'] + "\n" +
              '文件大小:' + str(filesize) + 'M' + "\n" +
              failure + "\n")
        dicts = [url, failure, failure]
        return dicts


def download_app():
    print("downloading with requests")
    read = ReadIni(conftest.userinfo_dir)
    url = read.get_value('download_url', 'App')
    r = requests.get(url)
    print(r)
    # with open("code3.zip", "wb") as code:
    #     #     code.write(r.content)


if __name__ == '__main__':
    read = ReadIni(conftest.userinfo_dir)
    url = read.get_value('download_url', 'App')
    download_apk(1, url)
    start = datetime.now()
    end = datetime.now() - start
    print('用时：' + str(end))

