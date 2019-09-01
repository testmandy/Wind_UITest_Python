# coding=utf-8
# @Time    : 2019/7/9 13:13
# @Author  : Mandy
import ftplib
import os
import time
import zipfile

import conftest

ftp_host = '10.88.0.22'
ftp_username = 'test'
ftp_password = 'pass'


class MyFtp:

    def __init__(self):
        self.ftp = ftplib.FTP(ftp_host)
        self.filename = 'SkyVPNDebugItunes.ipa'
        self.local_screen_path = conftest.screenshots_dir
        self.remote_path = r'/Ad_Screenshot/'
        now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 压缩后文件夹的名字
        self.zip_name = "android_screenshot_" + now_time + '.zip'
        self.zip_file = self.local_screen_path + self.zip_name

    def login(self, user, password):
        self.ftp.login(user, password)
        # print(self.ftp.welcome)

    def zip_file_folder(self, zip_file_dir, zip_name):
        """
        压缩指定文件夹
        :param zip_file_dir: 目标文件夹路径
        :param zip_name: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(zip_file_dir):
            # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = dirpath.replace(zip_file_dir, '')
            # 实现当前文件夹以及包含的所有文件的压缩
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                print('compressing', filename)
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print('compressing finished')
        z.close()

    def zip_files(self, zip_file_dir):
        """
        压缩指定文件夹下的所有文件
        :param zip_file_dir: 目标文件夹路径
        :param zip_name: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        zip_name = self.zip_name
        zip = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(zip_file_dir):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(zip_file_dir, '')
            for filename in filenames:
                print('[MyLog]--------Compressing', filename)
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        print('[MyLog]--------Compressing finished!')
        zip.close()

    def download_file(self, local_file, remote_file):  
        # 下载单个文件
        file_handler = open(local_file, 'wb')
        print(file_handler)
        # ftp.retrbinary("RETR %s" % (remote_file), file_handler.write)
        # 接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR ' + remote_file, file_handler.write)
        file_handler.close()
        return True

    def download_file_tree(self, local_dir, remote_dir):  
        # 下载整个目录下的文件
        print("[MyLog]--------remote_dir:", remote_dir)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        self.ftp.cwd(remote_dir)
        remote_names = self.ftp.nlst()
        print("[MyLog]--------remote_names", remote_names)
        for file in remote_names:
            local = os.path.join(local_dir, file)
            print(self.ftp.nlst(file))
            if file.find(".") == -1:
                if not os.path.exists(local):
                    os.makedirs(local)
                self.download_file_tree(local, file)
            else:
                self.download_file(local, file)
        self.ftp.cwd("..")
        return

    def upload_files(self, remote_path):
        """
        压缩指定文件夹
        :param: remote_path，远程文件夹路径
        :param: zip_file，需要上传的文件
        :return: 无
        """
        buf_size = 1024
        # 选择操作目录
        self.ftp.cwd(remote_path)
        # 列出目录文件
        # self.ftp.retrlines('LIST')
        # 打开要上传的文件
        upload_file = self.zip_name
        file_handler = open(upload_file, 'rb')
        # 要上传的远程文件地址+文件名
        filename = remote_path + upload_file
        print('[MyLog]--------Uploading', upload_file)
        # 上传文件
        self.ftp.storbinary('STOR %s' % os.path.basename(filename), file_handler, buf_size)
        self.ftp.set_debuglevel(0)
        print('[MyLog]--------Uploading finished! You can link the following address for details: ftp://' + ftp_host + self.remote_path)

    def remove_zip(self, zipname):
        os.remove(zipname)
        print('[MyLog]--------Remove zip success!')

    # 递归删除目录及其子目录下的文件
    def remove_files(self, path):
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):  # 判断是否是文件
                os.remove(path_file)
            else:
                self.remove_files(path_file)
        print('[MyLog]--------Remove files success!')


    def make_dir(self):
        os.makedirs(self.local_screen_path)

    def close(self):
        self.ftp.close()

    def main(self):
        self.login(ftp_username, ftp_password)
        self.zip_files(self.local_screen_path)
        # 上传文件
        self.upload_files(self.remote_path)
        self.remove_zip(self.zip_name)
        self.remove_files(conftest.screenshots_list)
        self.close()


# if __name__ == "__main__":
#     my_ftp = MyFtp()


