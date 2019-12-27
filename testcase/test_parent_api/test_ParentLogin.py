"""
author:xiaoma
datetime:2019/12/24 14:35
describe:

"""

import allure
import pytest

from params.parent_param_read_yaml import Login
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.header import HeaderUtil
from common import Log
log = Log.MyLog()


@allure.feature("家长端登录模块")
class TestLogin:

    @allure.title("正确的账号登录")
    def test_login_01(self):
        log.info("正确的账号登录")
        conf = Config()
        data = Login().yaml_data

        urls = data.url
        params = data.data
        headers = data.header

        api_url = conf.host_parent + urls[0]
        res =  RequestMethod().run_main("post",url=api_url, data=params[0], header=headers[0])
        op_header = HeaderUtil(res)
        op_header.write_parent_header()
        log.info("请求数据：" + str(params[0]))
        assert Assertions().assert_in("success", res)

    @allure.title("错误的账号登录")
    def test_login_02(self):
        log.info("错误的账号登录")
        conf = Config()
        data = Login().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        api_url = conf.host_parent + urls[1]
        res = RequestMethod().run_main("post", url=api_url, data=params[1], header=headers[1])
        log.info("请求数据：" + str(params[1]))
        assert Assertions().assert_in("密码错误", res)

    @allure.title("不存在的账号登录")
    def test_login_03(self):
        log.info("不存在的账号登录")
        conf = Config()
        data = Login().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求体数据：" + str(params[2]))
        api_url = conf.host_parent + urls[2]
        res = RequestMethod().run_main("post", url=api_url, data=params[2], header=headers[2])
        assert Assertions().assert_in("登录用户不存在", res)