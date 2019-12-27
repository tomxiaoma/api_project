"""
author:xiaoma
datetime:2019/12/26 16:27
describe:

"""
import allure
from params.parent_param_read_yaml import UpdatePasswordByPasswordMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("通过旧密码修改密码")
class TestUpdatePasswordByPasswordMutation:

    @allure.title("通过旧密码修改密码")
    def test_update_password_by_password_mutation(self):
        log.info("通过旧密码修改密码")
        conf = Config()
        data = UpdatePasswordByPasswordMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('code', str(res))
