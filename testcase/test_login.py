import allure
import pytest

from params.param_read_yaml import Login
from config.config import Config
from base import request_method
from common import Assert
from common.header import HeaderUtil
from common import Log
log = Log.MyLog()


@allure.feature("教师端登录模块")
class TestLogin:

    @allure.title("正确的账号登录")
    def test_login_01(self):
        log.info("正确的账号登录")
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        res = request.run_main("post",url=api_url, data=params[0], header=headers[0])
        op_header = HeaderUtil(res)
        op_header.write_teacher_header()
        log.info("请求数据：" + str(params[0]))
        assert test.assert_in("success", res)
        log.info("返回数据："+res)

    @allure.title("错误的账号登录")
    def test_login_02(self):
        log.info("错误的账号登录")
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        res = request.run_main("post", url=api_url, data=params[1], header=headers[1])
        log.info("请求数据：" + str(params[1]))
        assert test.assert_in("密码错误", res)
        log.info("返回数据：" + res)

    @allure.title("不存在的账号登录")
    def test_login_03(self):
        log.info("不存在的账号登录")
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求体数据：" + str(params[2]))

        api_url = req_url + urls[2]
        res = request.run_main("post", url=api_url, data=params[2], header=headers[2])
        assert test.assert_in("登录用户不存在", res)
        log.info("返回数据：" + res)









