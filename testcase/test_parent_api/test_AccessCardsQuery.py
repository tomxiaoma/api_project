"""
author:xiaoma
datetime:2019/12/26 17:30
describe:

"""
import allure
from params.parent_param_read_yaml import AccessCardsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("我的考勤卡查询")
class TestAccessCardsQuery:

    @allure.title("我的考勤卡查询")
    def test_access_cards_query(self):
        log.info("我的考勤卡查询")
        conf = Config()
        data = AccessCardsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('accessCards', str(res))
