"""
author:xiaoma
datetime:2019/12/27 10:47
describe:

"""
import allure
from params.parent_param_read_yaml import GuardiansQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("邀请家人页面查询")
class TestGuardiansQuery:

    @allure.title("邀请家人页面查询")
    def test_guardians_query(self):
        log.info("邀请家人页面查询")
        conf = Config()
        data = GuardiansQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('妈妈', str(res))
