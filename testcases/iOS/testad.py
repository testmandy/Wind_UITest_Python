# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy

import time
import unittest
from common.base_driver import BaseDriver
from common.my_ftp import MyFtp
from utils.dos_cmd import DosCmd
from utils.operation import Operation
from utils.server import Server


# 继承unittest.TestCase
class ShowAds:

    def __init__(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global operation, driver
        server = Server()
        server.main('ios')
        print("debug now……")
        base_driver = BaseDriver(0)
        print(base_driver)
        driver = base_driver.ios_driver()
        # 实例化Operation
        operation = Operation(driver)

    # @classmethod
    # def tearDownClass(cls):
    #     # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     my_ftp = MyFtp()
    #     my_ftp.main()
    #     print(u'关闭driver')
    #     driver.quit()
    #
    # def tearDown(self):
    #     # 每个测试用例执行之后做操作
    #     print(u'用例执行后')
    #     flag = operation.find_element("More_More_tab")
    #     print(flag)
    #     while flag is False:
    #         operation.tap_test("back_button")
    #         flag = operation.find_element("More_More_tab")
    #     print(u'用例执行完成，开始执行下一个')
    #
    # def setUp(self):
    #     # 每个测试用例执行之前做操作
    #     print(u'用例执行前')

    def test_message_list(self):
        # 点击Contacts--More--Messages--More--Messages
        operation.waiting_click(3, "Contact_Contact_tab")
        operation.waiting_click(1, "More_More_tab")
        operation.waiting_click(1, "Messages_Messages_tab")
        operation.waiting_click(1, "More_More_tab")
        operation.waiting_click(1, "Messages_Messages_tab")
        # 获取截屏
        operation.capture("Message_list")

    def test_team(self):
        # 点击小秘书TalkU Team
        operation.waiting_click(3, "Messages_TalkU_Team", 0)
        # 获取截屏
        operation.capture("Team")
        # 返回上一页
        operation.waiting_click(3, "Messages_chat_back_button")
        # 获取截屏
        operation.capture("Message_list2")

    def test_sms(self):
        # 点击写短信
        operation.waiting_click(3, "Messages_write_button")
        # 点击第一个美国号码
        operation.waiting_click(3, "Messages_number_list", 1)
        # 获取截屏
        operation.capture("SMS")
        # 返回上一页
        operation.waiting_click(3, "Messages_chat_back_button")

    def test_connect(self):
        # 点击Connect
        operation.waiting_click(3, "Connect_Connect_tab")
        # 获取截屏
        operation.capture("Connect")

    def test_check_result(self):
        # 点击Connect
        operation.waiting_click(3, "Connect_Connect_tab")
        # 向上滑动
        operation.swipe_on('up')
        # 点击Lottery
        operation.waiting_click(3, "Connect_lottery")
        # 点击Test My Luck
        operation.waiting_click(3, "Lottery_check_result_button")
        # 获取截屏
        operation.capture("Lottery")
        # 今天首次购买彩票
        operation.waiting_click(3, "Lottery_claim_prize_button")
        # 获取截屏
        operation.capture("Lottery_loading")
        # 关闭过渡界面广告
        operation.waiting_click(3, "Common_loading_close")
        # 返回上一页
        operation.waiting_click(1, "Lottery_lottry_back_button")
        # 购买彩票
        operation.waiting_click(1, "Lottery_purchase_ticket")
        # 获取截屏
        operation.capture("Lottery_loading2")
        # 关闭过渡界面广告
        operation.waiting_click(3, "Common_loading_close")
        # 点击Boost your luck
        operation.waiting_click(3, "Lottery_boost_luck_button")
        # 获取appwall截屏
        operation.capture("appwall")


    def test_buy_lottery(self):
        # 点击Connect
        operation.waiting_click(3, "Connect_Connect_tab")
        # 向上滑动
        operation.swipe_on('up')
        # 点击Lottery
        operation.waiting_click(3, "Connect_lottery")
        # 获取截屏
        operation.capture("Lottery")
        # 点击Test My Luck
        operation.waiting_click(3, "Lottery_test_luck_button")
        # 今天首次购买彩票
        operation.waiting_click(3, "Lottery_purchase_ticket")
        # 获取截屏
        operation.capture("Lottery_loading")

    def test_appwall(self):
        # 点击Connect
        operation.waiting_click(3, "Connect_Connect_tab")
        # 向上滑动
        operation.swipe_on('up')
        # 点击Lottery
        operation.waiting_click(3, "Connect_lottery")
        # 点击Boost your luck
        operation.waiting_click(3, "Lottery_boost_luck_button")
        # 获取appwall截屏
        operation.capture("appwall")

    def test_claim_prize(self):
        # 点击Connect
        operation.waiting_click(3, "Connect_Connect_tab")
        # 向上滑动
        operation.swipe_on('up')
        # 点击Lottery
        operation.waiting_click(3, "Connect_lottery")
        # 点击Boost your luck
        operation.waiting_click(3, "Lottery_boost_luck_button")
        # 获取appwall截屏
        operation.capture("appwall")


    def test_redeem(self):
        # 点击More
        operation.waiting_click(3, "More_More_tab")
        # 点击Redeem
        operation.waiting_click(3, "More_Redeem")
        # 获取截屏
        operation.capture("Redeem")
        # 返回上一页
        operation.waiting_click(3, "More_redeem_back_button")

    def test_check_in(self):
        # 点击More
        operation.waiting_click(3, "More_More_tab")
        # 点击Get Free Credits
        operation.waiting_click(3, "More_GetMoreCredits")
        # 点击Check-in
        operation.waiting_click(3, "Free_Checkin")
        # 点击Check in Now
        operation.waiting_click(3, "Free_CheckinNow")
        # 获取截屏
        operation.capture("GetCredits")
        time.sleep(5)
        # 获取截屏
        operation.capture("GetCredits2")
        # 点击关闭小黑屏幕
        operation.waiting_click(3, "Common_FN_ad_close")
        # 点击关闭全屏广告
        operation.waiting_click(3, "Common_AM_close_button")
        # 获取截屏
        operation.capture("GetCredits3")
        # 返回上一页
        operation.waiting_click(3, "Free_checkin_back_button")

    def test_feeling_lucky(self):
        # 点击More
        operation.waiting_click(3, "More_More_tab")
        # 点击Get Free Credits
        operation.waiting_click(3, "More_GetMoreCredits")
        # 点击Feeling lucky
        operation.waiting_click(3, "Free_FeelingLucky")
        # 获取截屏
        operation.capture("feelingLucky")
        # 点击Get More Credits
        operation.waiting_click(3, "Free_FeelingLucky_GetMore")
        time.sleep(2)
        # 获取截屏
        operation.capture("feellucky_loading")
        time.sleep(5)
        # 获取截屏
        operation.capture("feellucky_end")
        # 点击关闭全屏广告
        operation.waiting_click(3, "Common_AM_close_button")
        # 强行关闭弹窗
        driver.switch_to.alert.accept()
        # 获取截屏
        operation.capture("feellucky_close")

    def test_lucky_box(self):
        # 点击More
        operation.waiting_click(3, "More_More_tab")
        # 点击Get Free Credits
        operation.waiting_click(3, "More_GetMoreCredits")
        # 点击红包按钮
        operation.waiting_click(10, "Free_luckybox_button")
        # 获取截屏
        operation.capture("Luckybox")
        # 获取截屏
        operation.capture("Luckybox2")


if __name__ == '__main__':
    show = ShowAds()
    show.test_appwall()