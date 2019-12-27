"""
author:xiaoma
datetime:2019/12/13 11:42
describe:

"""
import allure
from params.teacher_param_read_yaml import MessageListQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("消息列表查询")
class TestMessageListQuery:

    @allure.title("消息列表查询")
    def test_message_list_query(self):
        log.info("消息列表查询")
        conf = Config()
        data = MessageListQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('pageInfo', str(res))
