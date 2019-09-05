# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy
import logging
import os
import threading
import time

import conftest
from utils.dos_cmd import DosCmd

# 创建Logger
from common.write_userconfig import WriteUserConfig

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.write_file = WriteUserConfig()
        self.log_path = conftest.log_dir

    def get_devices(self):
        """
        获取设备信息
        :return:设备列表devices_list
        """
        devices_list = []
        time.sleep(2)
        try:
            result_list = self.dos.excute_cmd_result("adb devices")
            print("[MyLog]--------The length of the result is: " + str(len(result_list)) + "----------------")
            print("[MyLog]--------The results of [adb devices] is: " + str(result_list))
            if len(result_list) >= 2:
                for i in result_list:
                    if 'List' in i:
                        continue
                    devices_info = i.split("\t")
                    time.sleep(2)
                    try:
                        if devices_info[-1] == 'device':
                            devices_list.append(devices_info[0])
                    except Exception as msg:
                        print(u"[MyLog]--------获取device失败%s" % msg)
                    else:
                        time.sleep(2)
                return devices_list
            else:
                print(u'[MyLog]--------没有连接的设备，请检查……')
                quit()
        except Exception as msg:
            print(u"启动adb异常%s" % msg)
        time.sleep(2)

    def port_is_used(self, port_num, platform=None):
        """
        判断端口是否被占用
        :param platform: 平台：ios/android
        :param port_num: 检查的端口号
        :return:布尔值flag
        """
        if platform is None:
            command = "netstat -ano | findstr " + str(port_num)
        else:
            command = "netstat -anp tcp | grep " + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list, platform):
        """
        生成可用端口
        :param platform: 平台：ios/android
        :param device_list: 连接的设备
        :param start_port: 起始端口号，如4700
        :return:
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port, platform) is not True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print(u"[MyLog]--------生成可用端口失败")
            return None

    def create_appium_command(self, i, device_list, platform=None):
        """
        appium -p 4723 -bp 4701 -U 159beaa8
        :return:command_list
        os.system会阻塞进程，为避免不影响执行下一步，在命令前面一定要加start
        改为用os.system("start appium -a 127.0.0.1 -p %s -U %s")
        """
        command_list = []
        time.sleep(2)
        appium_port_list = self.create_port_list(4700, device_list, platform)
        bootstrap_port_list = self.create_port_list(4900, device_list, platform)
        if platform is None:
            command = "start /b appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + \
                      " -U " + device_list[i] + " --session-override "
        else:
            command = "appium -a 127.0.0.1 -p " + str(appium_port_list[i]) + " --session-override "
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]),
                                   str(appium_port_list[i]))
        return command_list

    def start_server(self, i, device_list, platform=None):
        """
        定义方法：启动appium server
        """
        start_appium_list = self.create_appium_command(i, device_list, platform)
        print("[MyLog]--------" + str(start_appium_list))
        self.dos.excute_cmd(start_appium_list[0])

    def kill_server(self):
        """
        定义方法：每次执行前先kill掉node进程
        """
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self, platform):
        """
        多线程，执行main方法
        step1：kill server
        step2：clear file(userconfig.yaml)
        step3：根据生成的 appium list 分线程执行 start server
        """
        if platform == 'android':
            android_device_list = self.get_devices()
            device_list = android_device_list
            self.kill_server()
        else:
            ios_device_list = ['iPhone Simulator']
            device_list = ios_device_list
        thread_list = []
        self.write_file.clear_data()
        try:
            len(device_list)
        except Exception as msg:
            print(u"[MyLog]--------设备读取异常%s" % msg)
        else:
            for i in range(len(device_list)):
                if platform is None:
                    appium_start = threading.Thread(target=self.start_server, args=(i, device_list))
                else:
                    appium_start = threading.Thread(target=self.start_server, args=(i, device_list, 'ios'))
                thread_list.append(appium_start)
            for j in thread_list:
                j.start()
            time.sleep(10)



