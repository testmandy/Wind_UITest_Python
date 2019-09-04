# coding=utf-8
# @Time    : 2019/9/3 15:48
# @Author  : Mandy
import os
import time

import configparser
from appium.webdriver.common.touch_action import TouchAction

import conftest
from utils.get_element import GetElement


class Operation:
    def __init__(self, driver):
        self.driver = driver
        print("[MyLog]--------Start to RUN testcase")
        # 实例化GetByLocal
        self.starter = GetElement()
        # 清除report文件
        self.delete_log()

    def capture(self, name):
        """
        定义截图方法
        """
        time.sleep(2)
        img_folder = conftest.screenshots_dir
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)

    def get_element(self, key):
        """
        获取页面元素
        :return:element
        """
        return self.starter.get_element(self.driver, key)

    def get_son_element(self, father_element, key):
        """
        获取父元素下的子元素
        :return:element
        """
        return self.starter.get_element(father_element, key)

    def waiting_click(self, timeout, key, i=None):
        """
        封装方法，等待几秒后再点击操作
        """
        time.sleep(timeout)
        if None == i:
            self.starter.get_element(self.driver, key).click()
        else:
            self.starter.get_element(self.driver, key)[i].click()

    def waiting_send_keys(self, timeout, key, message, i=None):
        """
        封装方法，等待几秒后再输入字符串
        """
        time.sleep(timeout)
        if None == i:
            self.starter.get_element(self.driver, key).send_keys(message)
        else:
            self.starter.get_element(self.driver, key)[i].send_keys(message)

    def find_element(self, key):
        """
        查看（判断）页面是否有某元素
        :return:True or False
        """
        time.sleep(1)
        element_info = str(self.starter.get_element(self.driver, key))
        print(element_info)
        if 'element' in element_info:
            flag = True
        else:
            flag = False
        return flag

    def get_size(self):
        """
        获取屏幕大小
        :return:屏幕的宽高 width, height
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self):
        """
        向左滑动
        设想size的返回类型为[100,200]
        """
        # 设想size的返回类型为[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    def swipe_right(self):
        """
        向右滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1)

    def swipe_up(self):
        """
        向上滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)

    def swipe_down(self):
        """
        向下滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self, direction):
        """
        传入方向值，实现一个方法在不同方向滑动
        """
        time.sleep(1)
        if direction == "left":
            self.swipe_left()
        elif direction == "right":
            self.swipe_right()
        elif direction == "up":
            self.swipe_up()
        else:
            self.swipe_down()

    def tap_test(self, key, waiting_time=1):
        """
        根据屏幕定位点击元素
        """
        time.sleep(waiting_time)
        # 设定系数，控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        x = int(self.starter.get_axis(key)[0])
        y = int(self.starter.get_axis(key)[1])
        a1 = x / 720
        b1 = y / 1280
        # 获取当前手机屏幕大小X,Y
        x0 = self.driver.get_window_size()['width']
        y0 = self.driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(a1 * x0, b1 * y0)])

    def test_long_press(self, key, waiting_time=1):
        """
        长按屏幕元素
        """
        time.sleep(waiting_time)
        action1 = TouchAction(self.driver)
        el = self.starter.get_element(self.driver, key)
        action1.long_press(el=el, duration=5000).wait(3000).perform()

    def del_file(self, path):
        """
        定义方法：删除文件夹下所有文件
        """
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.del_file(c_path)
            else:
                os.remove(c_path)

    def delete_log(self):
        """
        定义方法：创建文件夹，并清除垃圾文件
        """
        if not os.path.exists('output'):
            os.system(r'mkdir output')
        if not os.path.exists('report'):
            os.system(r'mkdir report')
        if not os.path.exists('testapp'):
            os.system(r'mkdir testapp')
        if not os.path.exists('screenshots'):
            os.system(r'mkdir screenshots')
        if not os.path.exists('allure_result'):
            os.system(r'mkdir allure_result')

        os.system(r'rm -f ./output/*.*')
        os.system(r'touch ./output/log.log')
        os.system(r'rm -f ./report/*.*')
        os.system(r'rm -f ./testapp/*.*')
        os.system(r'rm -f ./screenshot/*.*')
        os.system(r'rm -f ./allure_result/*.*')

    def modify_env_config(self, app, env, platform, app_download_path):
        config_env_file = os.path.join(conftest.config_dir, 'env.ini')
        cp = configparser.ConfigParser()
        cp.read(config_env_file, encoding="UTF-8")
        cp.set('env', 'env', env)
        cp.set('app', 'app_name', app)
        cp.set('app_platform', 'platform_name', platform)
        if platform == 'ios':
            var = env + '_' + 'ios_app'
            cp.set(app, var, app_download_path)
        cp.write(open(config_env_file, 'w'))
        if platform == 'android':
            self.download_android_app(app, env, app_download_path)

    def download_android_app(self, app, env, app_download_path):
        SRC_WEB = 'http://10.88.0.23/recent/'
        APP_DIR = './testapp/'
        if app == 'dingtone':
            DST_PRE = 'Dingtone'
        elif app == 'talku':
            DST_PRE = 'TalkU'
        elif app == 'telos':
            DST_PRE = 'Telos'
        SRC_APP = app_download_path + '_' + env + '.apk'
        DST_APP = DST_PRE + env.upper() + '.apk'
        SRC = SRC_WEB + SRC_APP
        DST = APP_DIR + DST_APP
        os.system(r'wget %s -O %s' % (SRC, DST))

