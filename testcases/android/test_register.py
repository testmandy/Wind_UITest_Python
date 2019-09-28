# coding=utf-8
# @Time    : 2019/9/6 14:01
# @Author  : Mandy
import os
import time

import allure
import pytest
import conftest
from common.base_driver import BaseDriver
from utils.operation import Operation
from utils.server import Server
from common.read_ini import ReadIni


def setup_module():
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    global operation, driver
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


@allure.feature('注册、完善信息')  # feature定义功能
@pytest.mark.usefixtures('close_window_before')
@pytest.mark.register
class TestRegister(object):
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

    def logout(self):
        # 点击我
        operation.waiting_click(1, "Tab_me")
        # 点击设置
        operation.waiting_click(1, "Me_cards", 3)
        # 点击退出登录
        operation.waiting_click(1, "Setting_logout")
        # 点击确定
        operation.waiting_click(1, "Common_submit")

    @allure.severity(1)
    @allure.story('注册功能')
    def test_register(self):
        # 若已登录则退出
        if self.is_login:
            self.logout()
        # 获取ini文件中的信息
        telephone = read.get_value('telephone')
        code = read.get_value('code')
        # 输入手机号
        operation.waiting_send_keys(3, "Register_telephone", telephone)
        # 输入验证码
        operation.waiting_send_keys(2, "Register_code", code, 0)
        # 获取截屏
        operation.capture("register")

    @allure.severity(2)
    @allure.story('完善信息')
    def test_info(self):
        # 点击头像
        operation.waiting_click(3, "Register_photo")
        # 点击拍摄照片
        operation.waiting_click(2, "Register_camera")
        # 拍照
        operation.tap_test('camera_shutter')
        # 点击确认
        operation.waiting_click(2, "Camera_ok")
        # 确认截取照片
        operation.waiting_click(2, "Camera_done")
        # 输入昵称
        operation.waiting_send_keys(5, "Register_nickname", "test_nickname")
        # 选择性别
        operation.waiting_click(2, "Register_man")
        # 选择生日
        operation.waiting_click(2, "Register_birthday")
        # 确认日期
        operation.waiting_click(2, "Day_sure")
        # 获取截屏
        operation.capture("test_info")
        # 点击保存
        operation.waiting_click(1, "Register_save")




