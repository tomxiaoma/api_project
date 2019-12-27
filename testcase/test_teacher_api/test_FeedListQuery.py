"""
author:xiaoma
datetime:2019/12/12 16:35
describe:

"""

import allure
from params.teacher_param_read_yaml import FeedListQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据班级ID查询在园时光列表")
class TestFeedListQuery:

    @allure.title("根据班级ID查询在园时光列表")
    def test_feed_list_query(self):
        log.info("根据班级ID查询在园时光列表")
        conf = Config()
        data = FeedListQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('hasNextPage', str(res))
