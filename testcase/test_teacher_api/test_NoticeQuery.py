"""
author:xiaoma
datetime:2019/12/13 11:43
describe:

"""
import allure
from params.teacher_param_read_yaml import NoticeQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据通知ID查询通知详情")
class TestNoticeQuery:

    @allure.title("根据通知ID查询通知详情")
    def test_new_message_list_query(self):
        log.info("根据通知ID查询通知详情")
        conf = Config()
        data = NoticeQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('confirmedStudents', str(res))
