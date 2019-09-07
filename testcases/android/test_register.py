# coding=utf-8
# @Time    : 2019/9/6 14:01
# @Author  : Mandy
import os
import time
import pytest
import conftest
from common.base_driver import BaseDriver
from utils.operation import Operation
from utils.server import Server, logger
from common.read_ini import ReadIni


@pytest.mark.usefixtures('connect_app')
@pytest.mark.usefixtures('close_driver')
@pytest.mark.register
class TestWind(object):
    @pytest.fixture(scope='function')
    def connect_app(self):
        logger.info('------------------setup----------------')
        # 实例化Operation
        global operation, read, driver
        server = Server()
        server.main('android')
        base_driver = BaseDriver(0)
        driver = base_driver.android_driver()
        read = ReadIni(conftest.userinfo_dir)
        operation = Operation(driver)
        print('[MyLog]--------DRIVER is starting NOW')
        self.close_window_before()

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

    @pytest.fixture(scope='function')
    def close_driver(self):
        pass
        yield
        # 运行结束后动作：上传FTP，关闭driver
        print(u'[MyLog]--------关闭driver')
        # my_ftp = MyFtp()
        # my_ftp.main()
        if driver is not None:
            driver.quit()

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
        if operation.find_element("Tab_main"):
            flag = True
        return flag

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

    def logout(self):
        operation.waiting_click(1, "Tab_me")



