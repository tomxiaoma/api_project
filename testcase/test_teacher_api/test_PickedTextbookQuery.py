"""
author:xiaoma
datetime:2019/12/13 11:43
describe:

"""
import allure
from params.teacher_param_read_yaml import PickedTextbookQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据班级ID查询精选教材")
class TestPickedTextbookQuery:

    @allure.title("根据班级ID查询精选教材")
    def test_picked_textbook_query(self):
        log.info("根据班级ID查询精选教材")
        conf = Config()
        data = PickedTextbookQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('textbooks', str(res))
