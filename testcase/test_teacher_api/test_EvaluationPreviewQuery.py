"""
author:xiaoma
datetime:2019/12/12 16:16
describe:
"""

import allure
from params.teacher_param_read_yaml import EvaluationPreviewQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据ID查看评价预览")
class TestEvaluationPreviewQuery:

    @allure.title("根据ID查看评价预览")
    def test_evaluation_preview_query(self):
        log.info("根据ID查看评价预览")
        conf = Config()
        data = EvaluationPreviewQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('title', str(res))