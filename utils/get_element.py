# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy
import conftest
from common.read_ini import ReadIni


class GetElement:
    def __init__(self):
        pass

    def get_axis(self, key):
        file_path = conftest.android_axis_dir
        read_ini = ReadIni(file_path)
        axis = read_ini.get_value(key)
        if axis is not None:
            x = axis.split(",")[0]
            y = axis.split(",")[1]
            return x, y
        else:
            return None

    def get_element(self, driver, key):
        """
        查找页面元素
        :return:查找结果element
        """
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        if local is not None:
            by = local.split(">")[0]
            location = local.split(">")[1]
            if by == "id":
                try:
                    return driver.find_element_by_id(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
                    return None
            elif by == "ids":
                try:
                    return driver.find_elements_by_id(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
            elif by == "className":
                try:
                    return driver.find_element_by_class_name(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
            elif by == "classNames":
                try:
                    return driver.find_elements_by_class_name(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
            elif by == "text":
                try:
                    return driver.find_element_by_link_text(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
            else:
                try:
                    return driver.find_element_by_xpath(location)
                except Exception as msg:
                    print(u"[MyLog]--------查找元素异常%s" % msg)
        else:
            return None

