"""
author:xiaoma
datetime:2019/12/16 15:34
describe:

"""
import allure
from params.teacher_param_read_yaml import TextBookListQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("课程列表查询")
class TestTextBookListQuery:

    @allure.title("课程列表查询")
    def test_text_book_list_query(self):
        log.info("课程列表查询")
        conf = Config()
        data = TextBookListQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('description', str(res))