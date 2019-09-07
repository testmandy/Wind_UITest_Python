# coding=utf-8
# @Time    : 2019/9/6 14:38
# @Author  : Mandy
import os
import shutil
from datetime import datetime
import requests
import conftest
from common.read_ini import ReadIni

read = ReadIni(conftest.userinfo_dir)
url = read.get_value('download_url', 'App')
filename = os.path.basename(url)
filename = filename.split('?')[0]
apk_path = os.path.join(conftest.apk_dir, filename)

# def Schedule(a,b,c):
#     '''''
#     a:已经下载的数据块
#     b:数据块的大小
#     c:远程文件的大小
#    '''
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print('%.2f%%' % per)
# def run():
#     # local = url.split('/')[-1]
#     local = os.path.join('/testapp', 'Python-2.7.5.tar.bz2')
#     urllib.urlretrieve(url, local, Schedule)


def download_apk(num, url):
    """
    下载文件
    :param url:下载链接
    :param num:索引值
    """
    global count, filename
    count = 0
    succeed = 'Succeed'
    failure = 'Failure'
    print('第' + str(num) + '条url:\n' + url)
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
        file = requests.get(url, headers=headers, timeout=100)

        with open(filename, 'wb') as apk:
            apk.write(file.content)
            print(succeed + "\n")
            count += 1
    else:
        print('文件类型:' + response.headers['Content-Type'] + "\n" +
              '文件大小:' + str(filesize) + 'M' + "\n" +
              failure + "\n")


def move_file():
    old_dir = os.path.join(conftest.project_dir, 'common', filename)
    new_dir = conftest.apk_dir
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    if os.path.exists(old_dir):
        shutil.move(old_dir, new_dir)
        print(old_dir, '\n', new_dir)


def download_and_move():
    download_apk(1, url)
    start = datetime.now()
    end = datetime.now() - start
    print('用时：' + str(end))
    move_file()


