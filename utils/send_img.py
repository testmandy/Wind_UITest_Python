# coding=utf-8
# @Time    : 2019/7/9 9:46
# @Author  : Mandy

import requests
import conftest


class sendImg:
    def __init__(self):
        self.img_path = conftest.screenshots_dir
        self.img_name = ""

    def send_Img(img_path, img_name, img_type='image/jpeg'):
        """
        :param img_path:图片的路径
        :param img_name:图片的名称
        :param img_type:图片的类型,这里写的是image/jpeg，也可以是png/jpg
        """
        # 自己想要请求的接口地址
        url = 'https://www.xxxxxxxxxx.com'
        # 以2进制方式打开图片

        with open(img_path + img_name, "rb")as f_abs:
            # 有些上传图片时可能会有其他字段,比如图片的时间什么的，这个根据自己的需要
            body = {
                'camera_code': (None, "商场"),
                # 图片的名称、图片的绝对路径、图片的类型（就是后缀）
                'image': (img_name, f_abs, img_type),
                "time": (None, "2019-01-01 10:00:00")
            }
            # 上传图片的时候，不使用data和json，用files
            response = requests.post(url=url, files=body).json
            return response

