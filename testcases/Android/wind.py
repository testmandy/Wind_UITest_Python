# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy

import time
import unittest

import conftest
from common.base_driver import BaseDriver
from common.my_ftp import MyFtp
from utils.operation import Operation
from utils.server import Server
from common.read_ini import ReadIni


# 继承unittest.TestCase
class Wind(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global operation, driver, read
        # 调用get_driver
        read = ReadIni(conftest.userinfo_dir)
        server = Server()
        server.main()
        base_driver = BaseDriver(0)
        driver = base_driver.android_driver()
        # 实例化Operation
        operation = Operation(driver)

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        my_ftp = MyFtp()
        my_ftp.main()
        print(u'[MyLog]--------关闭driver')
        driver.quit()

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u'[MyLog]--------用例执行后')
        flag = operation.find_element("Tab_main")
        print(flag)
        while flag is False:
            operation.waiting_click(2, "Common_back_button")
            flag = operation.find_element("Tab_main")
        print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print ('------------------setup----------------')

    def register(self):
        # 点击注册手机号
        telephone = read.get_value('telephone')
        password = read.get_value('password')
        operation.waiting_send_keys(3, "Register_telephone", telephone)
        operation.waiting_send_keys(1, "Register_code", password)
        # 获取截屏
        operation.capture("register")

    def test_info(self):
        # 点击头像
        operation.waiting_click(3, "Register_photo")
        # 点击拍摄照片
        operation.waiting_click(2, "Register_camera")
        # 拍照
        # 点击确认

        # 输入昵称
        operation.waiting_send_keys(3, "Register_nickname", "test_nickname")
        # 选择性别
        operation.waiting_click(1, "Register_man")
        # 选择生日
        operation.waiting_click(1, "Register_birthday")
        # 确认日期
        operation.waiting_click(1, "")
        # 获取截屏
        operation.capture("test_info")
        # 点击保存
        operation.waiting_click(1, "Register_save")


    def test_match(self):
        # 点击匹配
        operation.waiting_click(3, "Tab_main")
        # 获取截屏
        operation.capture("test_match_1")
        # 点击吹走
        operation.waiting_click(3, "Match_clean")
        # 获取截屏
        operation.capture("test_match_2")
        # 点击卡片red
        operation.waiting_click(3, "Match_card_red")
        # 获取截屏
        operation.capture("test_match_3")
        # 返回
        operation.waiting_click(3, "Common_back_button")
        # 点击卡片yellow
        operation.waiting_click(3, "Match_card_yellow")
        # 返回
        operation.waiting_click(3, "Common_back_button")
        # 点击卡片blue
        operation.waiting_click(3, "Match_card_blue")



        # 获取截屏
        operation.capture("test_match")
        # 返回上一页
        operation.waiting_click(3, "Common_back_button")


