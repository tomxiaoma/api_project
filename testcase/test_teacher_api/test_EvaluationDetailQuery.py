"""
author:xiaoma
datetime:2019/12/6 18:11
describe:

"""

import allure
from params.teacher_param_read_yaml import EvaluationDetailQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据评价ID查询评价详情")
class TestEvaluationDetailQuery:

    @allure.title("根据评价ID查询评价详情")
    def test_evaluation_detail_query(self):
        log.info("根据评价ID查询评价详情")
        conf = Config()
        data = EvaluationDetailQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().run_main("post",url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('term', str(res))
