# coding=utf-8
# @Time    : 2019/9/3 15:00
# @Author  : Mandy
import os
import time

import allure
import pytest
import conftest
from common.base_driver import BaseDriver
from utils.operation import Operation
from utils.server import Server, logger
from common.read_ini import ReadIni


def setup_module():
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    global operation, driver
    # 调用get_driver
    base_driver = BaseDriver()
    driver = base_driver.android_driver()
    # 实例化Operation
    operation = Operation(driver)
    print('[MyLog]--------OPERATION is inited NOW')


def teardown_module():
    # 运行结束后动作：上传FTP，关闭driver
    print(u'[MyLog]--------关闭driver')
    # my_ftp = MyFtp()
    # my_ftp.main()
    if driver is not None:
        driver.quit()


@allure.feature('app主功能')  # feature定义功能
@pytest.mark.usefixtures('close_window_before')
@pytest.mark.mine
class TestWind(object):
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

    def back_home(self):
        flag = operation.find_element("Common_back_button")
        while flag:
            operation.waiting_click(1, "Common_back_button")

    def is_login(self):
        flag = None
        self.close_window()
        if operation.find_element("Register_telephone"):
            flag = False
        elif operation.find_element("Tab_main"):
            flag = True
        return flag

    @allure.severity(1)
    @allure.story('人设卡')
    def test_card(self):
        # 点击我
        operation.waiting_click(1, "Tab_me")
        # 点击卡片-人设卡
        operation.waiting_click(1, "Me_cards", 0)
        # 获取截屏
        operation.capture("test_card")
        # 点击添加人设卡
        operation.waiting_click(1, "Image_add_button")
        # 获取截屏
        operation.capture("test_card")
        # 选择一个标签主题
        operation.waiting_click(2, "Image_labels")
        # 点击拍照
        operation.waiting_click(1, "Image_camera")
        self.close_window()
        # 输入文字
        operation.waiting_send_keys(1, "Image_text", "this is me")
        # 获取截屏
        operation.capture("test_card")
        # 点击发布按钮
        operation.waiting_click(1, "Image_submit")
        # 发布成功，点击确定
        operation.waiting_click(3, "Image_success")
        # 若当前不在一级页面，点击返回
        while operation.find_element("Common_back_button"):
            operation.waiting_click(1, "Common_back_button")


    @allure.severity(2)
    @allure.story('发布闪现')
    def test_props(self):
        # 点击我
        operation.waiting_click(1, "Tab_me")
        # 点击卡片-人设卡
        operation.waiting_click(1, "Me_cards", 1)
        # 获取截屏
        operation.capture("test_props")
        # 屏幕上滑
        operation.swipe_on('up')
        # 获取截屏
        operation.capture("test_me")
        # 若当前不在一级页面，点击返回
        while operation.find_element("Common_back_button"):
            operation.waiting_click(1, "Common_back_button")

    @allure.severity(3)
    def test_question(self):
        # 点击我
        operation.waiting_click(1, "Tab_me")
        # 点击卡片-真心话
        operation.waiting_click(1, "Me_cards", 2)
        # 获取截屏
        operation.capture("test_question")
        # 若发现编辑按钮则点击
        if operation.find_element("Offline_edit_button"):
            operation.waiting_click(2, "Offline_edit_button")
        else:
            operation.waiting_click(2, "Offline_add_button")
        # 获取截屏
        operation.capture("test_question")
        # 输入问题
        operation.waiting_send_keys(2, "Offline_question", "this is offline question")
        # 输入答案
        operation.waiting_send_keys(2, "Offline_answer", "this is offline answer")
        # 点击完成
        operation.waiting_click(2, "Offline_submit")
        # 添加完成，点击确定
        operation.waiting_click(2, "Common_submit")
        # 若当前不在一级页面，点击返回
        while operation.find_element("Common_back_button"):
            operation.waiting_click(1, "Common_back_button")

    @allure.severity(4)
    def test_settings(self):
        # 点击我
        operation.waiting_click(1, "Tab_me")
        # 点击卡片-设置
        operation.waiting_click(1, "Me_cards", 3)
        # 获取截屏
        operation.capture("test_settings")
        # 若当前不在一级页面，点击返回
        while operation.find_element("Common_back_button"):
            operation.waiting_click(1, "Common_back_button")


