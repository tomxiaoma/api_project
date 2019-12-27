"""
author:xiaoma
datetime:2019/12/19 10:59
describe:

"""

import allure
from params.teacher_param_read_yaml import DeleteNoticeMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
import pytest
from common import Log
log = Log.MyLog()


@allure.feature("老师删除通知")
class TestDeleteNoticeMutation:

    @pytest.mark.skip("跳过TestDeleteNoticeMutation（删除通知测试）")
    @allure.title("老师删除通知")
    def test_delete_notice_mutation(self):
        log.info("老师删除通知")
        conf = Config()
        data = DeleteNoticeMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('', str(res))