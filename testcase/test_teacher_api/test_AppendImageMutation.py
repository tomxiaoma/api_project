"""
author:xiaoma
datetime:2019/12/17 11:29
describe:

"""
import allure
import pytest
from params.teacher_param_read_yaml import AppendImageMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("在园时光动态补发照片")
class TestAppendImageMutation:

    @pytest.mark.skip("TestAppendImageMutation（在园时光动态补发照片）暂时不进行测试")
    @allure.title("在园时光动态补发照片")
    def test_append_image_mutation(self):
        log.info("在园时光动态补发照片")
        conf = Config()
        data = AppendImageMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('', str(res))
