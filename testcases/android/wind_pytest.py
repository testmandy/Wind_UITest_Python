# coding=utf-8
# @Time    : 2019/9/3 15:00
# @Author  : Mandy

import time
import pytest
import conftest
from common.base_driver import BaseDriver
from utils.operation import Operation
from utils.server import Server
from common.read_ini import ReadIni


def setup_module():
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    global operation, driver, read
    # 调用get_driver
    read = ReadIni(conftest.userinfo_dir)
    server = Server()
    server.main('android')
    base_driver = BaseDriver(0)
    driver = base_driver.android_driver()
    # 实例化Operation
    operation = Operation(driver)
    print('[MyLog]--------OPERATION is inited NOW')


def teardown_module():
    # 运行结束后动作：上传FTP，关闭driver
    print(u'[MyLog]--------关闭driver')
    # my_ftp = MyFtp()
    # my_ftp.main()
    driver.quit()


@pytest.mark.usefixtures('close_window_before')
class TestWind(object):
    # def setup_function(self):
    #     print('[MyLog]------------------setup----------------')
    #     # 每个测试用例执行之前做操作
    #     self.close_window()
    #     # 若当前不在一级页面，点击返回
    #     self.back_home()

    # def teardown_function(self):
    #     # 每个测试用例执行之后做操作
    #     print(u'[MyLog]--------用例执行后')
    #     self.back_home()
    #     print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def close_window(self):
        # 若出现引导页则点击
        # operation.tap_test("center_location")
        flag1 = operation.find_element("Common_cancel")
        flag2 = operation.find_element("Common_confirm_button")
        flag3 = operation.find_element("Permission_allow_button")
        # 循环检查当前是否出现弹窗
        while flag1 or flag2 or flag3:
            if flag1:
                operation.waiting_click(1, "Common_cancel")
            elif flag2:
                operation.waiting_click(1, "Common_confirm_button")
            elif flag3:
                operation.waiting_click(1, "Permission_allow_button")
            flag1 = operation.find_element("Common_cancel")
            flag2 = operation.find_element("Common_confirm_button")
            flag3 = operation.find_element("Permission_allow_button")

    @pytest.fixture(scope='module')
    def close_window_before(self):
        # 每个测试用例执行之前做操作
        # 若弹出升级提示则取消
        if operation.find_element("Common_cancel"):
            operation.waiting_click(1, "Common_cancel")
        # 若出现引导页则点击
        while operation.find_element("Tab_main") is False:
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

    def back_home(self):
        flag = operation.find_element("Common_back_button")
        while flag:
            operation.waiting_click(1, "Common_back_button")

    def is_login(self):
        flag = None
        self.close_window()
        if operation.find_element("Tab_main"):
            flag = True
        return flag

    @pytest.mark.skip
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

    @pytest.mark.skip
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
        # 获取截屏
        operation.capture("test_chat")
        # 点击离线聊天包
        while operation.find_element("Chat_offline_button"):
            operation.waiting_click(2, "Chat_offline_button")
            # 解锁真心话
            operation.waiting_click(2, "Chat_question_choose", 2)
            time.sleep(2)
        # 点击录音
        operation.waiting_click(1, "Chat_voice")
        # 若出现弹窗提示，点击确认
        self.close_window()
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
        self.close_window()
        # 点击第一个地址
        operation.waiting_click(1, "Chat_address", 0)
        # 点击确定
        operation.waiting_click(1, "Common_right_button")
        # 点击提问
        operation.waiting_click(1, "Chat_question")
        # 点击直接提问
        operation.waiting_click(1, "Chat_ask")
        # 输入问题
        operation.waiting_send_keys(1, "Chat_input_question", "Do you like travelling? ")
        # 点击发送
        operation.waiting_click(1, "Common_submit")
        # 点击道具
        operation.waiting_click(1, "Chat_tools")
        # 点击使用交换卡
        operation.waiting_click(1, "Chat_card_exchange")
        # 返回上一页
        operation.waiting_click(1, "Common_back_button")

    def test_map(self):
        # 点击闪现
        operation.waiting_click(1, "Tab_map")
        # 获取截屏
        operation.capture("test_map")
        # 点击列表
        operation.waiting_click(1, "Map_list")
        # 获取截屏
        operation.capture("test_map")
        # 点击联系人
        operation.waiting_click(1, "Map_list_card")
        # 获取截屏
        operation.capture("test_map")
        # 返回上一页
        operation.waiting_click(1, "Map_list")
        # 点击地图
        operation.waiting_click(1, "Common_back_button")
        # 若有闪现卡，则点击闪现卡
        if operation.find_element("Map_card"):
            operation.waiting_click(1, "Map_card")
            # 获取截屏
            operation.capture("test_map")
            # 若有【去偶遇】按钮，点击去偶遇
            if operation.find_element("Card_chat"):
                operation.waiting_click(1, "Card_chat")
                # 获取截屏
                operation.capture("test_map")
                # 若有多张照片，点击不同照片
                if operation.find_element("Card_pic_one"):
                    operation.waiting_click(1, "Card_pic_one")
                if operation.find_element("Card_pic_one"):
                    operation.waiting_click(1, "Card_pic_two")
                if operation.find_element("Card_pic_one"):
                    operation.waiting_click(1, "Card_pic_three")


    def test_post(self):
        operation.waiting_click(1, "Tab_post")
        # 点击发布+


    def test_me(self):
        operation.waiting_click(1, "Tab_me")
        # 点击发布+


