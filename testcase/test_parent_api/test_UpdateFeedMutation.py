"""
author:xiaoma
datetime:2019/12/26 16:08
describe:

"""
import allure
from params.parent_param_read_yaml import UpdateFeedMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("编辑个人动态")
class TestUpdateFeedMutation:

    @allure.title("编辑个人动态")
    def test_update_feed_mutation(self):
        log.info("编辑个人动态")
        conf = Config()
        data = UpdateFeedMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('happenedAt', str(res))
