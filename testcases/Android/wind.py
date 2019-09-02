# coding=utf-8
# @Time    : 2019/9/3 15:00
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
        # 运行结束后动作：上传FTP，关闭driver
        # my_ftp = MyFtp()
        # my_ftp.main()
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
        if operation.find_element("Common_cancel"):
            # 若弹出升级提示则取消
            operation.waiting_click(1, "Common_cancel")
        flag = operation.find_element("Tab_main")
        # print(flag)
        while flag is False:
            # 若出现引导页则点击
            operation.tap_test("center_location")
            # 若出现弹窗提示，点击确认
            while operation.find_element("Common_confirm_button"):
                operation.waiting_click(1, "Common_confirm_button")
            # 若出现获取权限，点击确认
            while operation.find_element("Permission_allow_button"):
                operation.waiting_click(1, "Permission_allow_button")
            # 若当前不在一级页面，点击返回
            while operation.find_element("Common_back_button"):
                operation.waiting_click(1, "Common_back_button")
            flag = operation.find_element("Tab_main")
        print('[MyLog]------------------setup----------------')

    def test_register(self):
        # 获取ini文件中的信息
        telephone = read.get_value('telephone')
        code = read.get_value('code')
        # 输入手机号
        operation.waiting_send_keys(3, "Register_telephone", telephone)
        # 输入验证码
        operation.waiting_send_keys(2, "Register_code", code, 0)
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
        operation.waiting_click(2, "Tab_main")
        # 获取截屏
        operation.capture("test_match_1")
        # 点击吹走
        operation.waiting_click(2, "Match_clean")
        # 获取截屏
        operation.capture("test_match_2")
        # 点击卡片red
        operation.waiting_click(2, "Match_card_red")
        # 获取截屏
        operation.capture("test_match_3")
        # 返回
        operation.waiting_click(2, "Common_back_button")
        # 点击卡片yellow
        operation.waiting_click(2, "Match_card_yellow")
        # 返回
        operation.waiting_click(2, "Common_back_button")
        # 点击卡片blue
        operation.waiting_click(2, "Match_card_blue")
        # 获取截屏
        operation.capture("test_match")
        # 返回上一页
        operation.waiting_click(2, "Common_back_button")

    def test_chat(self):
        # 点击爆灯yellow
        operation.waiting_click(2, "Match_button_yellow")
        # 点击离线聊天包
        while operation.find_element("Chat_offline_button"):
            operation.waiting_click(2, "Chat_offline_button")
            # 解锁真心话
            operation.waiting_click(2, "Chat_question_choose", 2)
            time.sleep(2)
        # 点击录音
        operation.waiting_click(1, "Chat_voice")
        # 若出现弹窗提示，点击确认
        while operation.find_element("Common_confirm_button"):
            operation.waiting_click(1, "Common_confirm_button")
        # 若出现获取权限，点击确认
        while operation.find_element("Permission_allow_button"):
            operation.waiting_click(1, "Permission_allow_button")
        # 长按录音
        operation.test_long_press("Chat_record")
        # 点击键盘
        operation.waiting_click(1, "Chat_keyboard")
        # 输入文字
        operation.waiting_send_keys(1, "Chat_input", "1234567890")
        # 点击发送
        operation.waiting_click(1, "Chat_send_text")
        # 点击加号
        operation.waiting_click(1, "Chat_more")
        # 点击位置
        operation.waiting_click(1, "Chat_position")
        # 若出现获取权限，点击确认
        while operation.find_element("Permission_allow_button"):
            operation.waiting_click(1, "Permission_allow_button")
        # 点击第一个地址
        operation.waiting_click(1, "Chat_address", 0)
        # 点击确定
        operation.waiting_click(1, "Common_right_button")
        # 点击提问
        operation.waiting_click(1, "Chat_question")
        # 点击直接提问
        operation.waiting_click(1, "Chat_ask")
        # 输入问题
        operation.waiting_send_keys(1, "Chat_input_question", "你喜欢旅行吗？")
        # 点击发送
        operation.waiting_click(1, "Common_submit")
        # 点击道具
        operation.waiting_click(1, "Chat_tools")
        # 点击使用交换卡
        operation.waiting_click(1, "Chat_card_exchange")
        # 返回上一页
        operation.waiting_click(1, "Common_back_button")







