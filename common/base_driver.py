# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy
import time

from appium import webdriver
from common.write_userconfig import WriteUserConfig


class BaseDriver:
    def __init__(self, i):
        write_file = WriteUserConfig()
        self.device = write_file.get_value('device' + str(i), 'deviceName')
        self.port = write_file.get_value('device' + str(i), 'port')

    def android_driver(self):
        # server = Server()
        # port = server.port
        print("[MyLog]--------Connected Device of Android driver: " + self.device)
        capabilities = {
            "platformName": "Android",
            "deviceName": self.device,
            # 可以通过newcommandtimeout将超时时间改长，超时时间可按照实际情况自定义
            "newCommandTimeout": "2000",
            "app": "E:\\360Downloads\\shenmefeng_105.apk",
            # 获取activity：aapt dump badging E:\360Downloads\shenmefeng_105.apk

            # "appWaitActivity": "com.wind.im.activity.SplashActivity",
            # "appWaitActivity": "com.wind.im.activity.LoginActivity",
            # "appWaitActivity": "cn.leancloud.chatkit.activity.LCIMConversationActivity",

            "appWaitActivity": "com.wind.im.activity.MainActivity",
            "appPackage": "com.wind.im",
            "noReset": "true"
        }
        try:
            driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
        except Exception as msg:
            print('[MyLog]--------启动driver发生异常' % msg)
        else:
            time.sleep(5)
            return driver

    def ios_driver(self):
        # 配置信息
        print("[MyLog]--------Connected Device of iOS driver: " + self.device)
        capability = {
            "newCommandTimeout": "2000",
            "automationName": "XCUITest",
            "platformName": "iOS",
            "platformVersion": "12.1",
            "deviceName": "iPhone Simulator",
            "udid": "31158BAD-B39C-476D-B6C0-1BFF874C53F9",
            "app": "/Users/destiny/Downloads/skyvpn.ipa",
            "noReset": "true"
        }
        try:
            driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capability)
        except Exception as msg:
            print(u'启动driver发生异常' % msg)
        else:
            time.sleep(5)
            return driver







