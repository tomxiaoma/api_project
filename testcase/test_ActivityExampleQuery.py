"""
author:xiaoma
datetime:2019/12/3 14:48
describe:

"""

import allure
import pytest

from params.param_read_yaml import ActivityExampleQuery
from config.config import Config
from base import request_method
from common import Consts
from common import Assert
from common import Log
log = Log.MyLog()


@allure.feature("教师端活动案例库")
class TestActivityExampleQuery:

    @allure.title("根据小班的班级ID查询小班活动范例库")
    def test_activity_example_small(self):
        conf = Config()
        data = ActivityExampleQuery().yaml_data
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头:"+str(headers))
        log.info("请求体："+str(params[0]))
        api_url = req_url + urls[0]
        response = request.post_method(url=api_url, data=params[0], header=headers[0])
        assert test.assert_in("游戏", str(response))

    @allure.title("根据中班的班级ID查询中班活动范例库")
    def test_activity_example_medium(self):
        conf = Config()
        data = ActivityExampleQuery().yaml_data
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头:" + str(headers))
        log.info("请求体：" + str(params[1]))
        api_url = req_url + urls[1]
        response = request.post_method(url=api_url, data=params[1], header=headers[1])
        assert test.assert_in("游戏", str(response))

    @allure.title("根据大班的班级ID查询大班活动范例库")
    def test_activity_example_large(self):
        conf = Config()
        data = ActivityExampleQuery().yaml_data
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头:" + str(headers))
        log.info("请求体：" + str(params[2]))
        api_url = req_url + urls[2]
        response = request.post_method(url=api_url, data=params[2], header=headers[2])
        assert test.assert_in("游戏", str(response))





