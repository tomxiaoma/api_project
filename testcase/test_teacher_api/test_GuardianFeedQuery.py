"""
author:xiaoma
datetime:2019/12/12 18:11
describe:

"""
import allure
from params.teacher_param_read_yaml import GuardianFeedQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据feed_id查询亲子完成情况")
class TestGuardianFeedQuery:

    @allure.title("根据feed_id查询亲子完成情况")
    def test_guardian_feed_query(self):
        log.info("根据feed_id查询亲子完成情况")
        conf = Config()
        data = GuardianFeedQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('creatorName', str(res))
