"""
author:xiaoma
datetime:2019/12/26 16:29
describe:

"""
import allure
import pytest
from params.parent_param_read_yaml import UpdatePasswordBySmsMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("通过短信验证码修改密码")
class TestUpdatePasswordBySmsMutation:

    @pytest.mark.skip("暂时跳过test_update_password_by_sms_mutation（通过短信验证码修改密码）测试")
    @allure.title("通过短信验证码修改密码")
    def test_update_password_by_sms_mutation(self):
        log.info("通过短信验证码修改密码")
        conf = Config()
        data = UpdatePasswordBySmsMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('happenedAt', str(res))
