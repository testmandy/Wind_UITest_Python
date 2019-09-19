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
    global operation, driver, read
    # 调用get_driver
    read = ReadIni(conftest.env_dir)
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
    if driver is not None:
        driver.quit()


@allure.feature('app主功能')  # feature定义功能
@pytest.mark.usefixtures('close_window_before')
@pytest.mark.map
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
    @allure.story('地图')
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



