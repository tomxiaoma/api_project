"""
author:xiaoma
datetime:2019/12/26 16:24
describe:

"""
import allure
from params.parent_param_read_yaml import UpdateGuardianRole
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("家长修改身份角色")
class TestUpdateGuardianRole:

    @allure.title("家长修改身份角色")
    def test_update_guardian_role(self):
        log.info("家长修改身份角色")
        conf = Config()
        data = UpdateGuardianRole().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('SUCCESS', str(res))
