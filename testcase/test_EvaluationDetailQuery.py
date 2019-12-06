"""
author:xiaoma
datetime:2019/12/6 18:11
describe:

"""

import allure
from params.param_read_yaml import EvaluationDetailQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据评价ID查询评价详情")
class TestBoxesQuery:

    @allure.title("根据评价ID查询评价详情")
    @allure.suite("根据评价ID查询评价详情")
    def test_test_boxes_query(self):
        log.info("根据评价ID查询评价详情")
        conf = Config()
        data = EvaluationDetailQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_debug + urls[0]
        res = RequestMethod().run_main("post",url=api_url, data=params[0], header=headers[0])
        log.info("返回结果：" + str(res))
        assert Assertions().assert_in('term', str(res))
