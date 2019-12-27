"""
author:xiaoma
datetime:2019/12/17 16:00
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteActivityMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()
import pytest


@allure.feature("删除在园时光")
class TestDeleteActivityMutation:

    @pytest.mark.skip("跳过删除在园时光测试（test_delete_activity_mutation）")
    @allure.title("删除在园时光")
    def test_delete_activity_mutation(self):
        log.info("删除在园时光")
        conf = Config()
        data = DeleteActivityMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('', str(res))
