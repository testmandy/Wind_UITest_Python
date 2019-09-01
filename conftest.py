# coding=utf-8
# @Time    : 2019/7/10 11:05
# @Author  : Mandy
import os
import logging
import logging.config


project_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(project_dir, 'logs\\')

report_dir = os.path.join(project_dir, 'report\\')

elements_dir = os.path.join(project_dir, 'elements')

android_elements_dir = os.path.join(elements_dir, 'android\\elements.ini')
android_axis_dir = os.path.join(elements_dir, 'android\\axis.ini')
userinfo_dir = os.path.join(elements_dir, 'android\\userinfo.ini')

screenshots_dir = os.path.join(project_dir, 'screenshots\\')
screenshots_list = os.path.join(project_dir, 'screenshots')

config_dir = os.path.join(project_dir, 'config')

userconfig_dir = os.path.join(config_dir, 'userconfig.yaml')




def get_logger():
    CONF_LOG = "../config/logging.ini"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()
