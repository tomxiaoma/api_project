"""
author:xiaoma
datetime:2019/12/26 15:43
describe:

"""
import allure
from params.parent_param_read_yaml import UnbindAccessCardMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("注销我的考勤卡")
class TestUnbindAccessCardMutation:

    @allure.title("注销我的考勤卡")
    def test_unbind_access_card_mutation(self):
        log.info("注销我的考勤卡")
        conf = Config()
        data = UnbindAccessCardMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('unbindAccessCard', str(res))
