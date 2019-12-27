"""
author:xiaoma
datetime:2019/12/26 18:33
describe:

"""
import allure
from params.parent_param_read_yaml import GuardianEvaluations
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("素质评价查询")
class TestGuardianEvaluations:

    @allure.title("素质评价查询")
    def test_guardian_evaluations(self):
        log.info("素质评价查询")
        conf = Config()
        data = GuardianEvaluations().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('大班上学期', str(res))
