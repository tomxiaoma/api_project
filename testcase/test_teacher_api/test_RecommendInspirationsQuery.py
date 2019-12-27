"""
author:xiaoma
datetime:2019/12/16 16:58
describe:

"""

import allure
from params.teacher_param_read_yaml import RecommendInspirationsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("灵感库推荐查询")
class TestRecommendInspirationsQuery:

    @allure.title("灵感库推荐查询")
    def test_recommend_inspirations_query(self):
        log.info("灵感库推荐查询")
        conf = Config()
        data = RecommendInspirationsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('popup', str(res))