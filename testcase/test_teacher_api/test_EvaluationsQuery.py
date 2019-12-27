"""
author:xiaoma
datetime:2019/12/12 16:26
describe:

"""

import allure
from params.teacher_param_read_yaml import EvaluationsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据班级ID查询评价列表")
class TestEvaluationsQuery:

    @allure.title("根据班级ID查询评价列表")
    def test_evaluations_query(self):
        log.info("根据班级ID查询评价列表")
        conf = Config()
        data = EvaluationsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('publishedAt', str(res))
