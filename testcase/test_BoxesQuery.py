"""
author:xiaoma
datetime:2019/12/3 14:48
describe:

"""
import allure
from params.param_read_yaml import BoxesQuery
from config.config import Config
from base import request_method
from common import Consts
from common import Assert
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()
import json


@allure.feature("教师端小红点")
class TestBoxesQuery:

    @allure.suite("教师端小红点查询")
    def test_test_boxes_query(self):
        log.info("根据班级ID获取教师端小红点")
        conf = Config()
        data = BoxesQuery()
        test = Assert.Assertions()
        request = request_method.RequestMethod()

        host = conf.host_debug
        req_url = host
        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = req_url + urls[0]
        res= request.post_method(url=api_url, data=params[0], header=headers)
        log.info("返回结果："+str(res))
        assert test.assert_in('happenedAt', str(res))





