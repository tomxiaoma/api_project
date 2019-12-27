"""
author:xiaoma
datetime:2019/12/26 16:37
describe:

"""
import allure
from params.parent_param_read_yaml import UpdatePhoneMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("修改手机号")
class TestUpdatePhoneMutation:

    @allure.title("修改手机号")
    def test_update_phone_mutation(self):
        log.info("修改手机号")
        conf = Config()
        data = UpdatePhoneMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('code', str(res))
