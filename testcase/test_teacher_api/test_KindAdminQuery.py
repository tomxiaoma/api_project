"""
author:xiaoma
datetime:2019/12/13 10:55
describe:

"""

import allure
from params.teacher_param_read_yaml import KindAdminQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("幼儿园管理员查询")
class TestKindAdminQuery:

    @allure.title("幼儿园管理员查询")
    def test_kind_admin_query(self):
        log.info("幼儿园管理员查询")
        conf = Config()
        data = KindAdminQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('administrators', str(res))
