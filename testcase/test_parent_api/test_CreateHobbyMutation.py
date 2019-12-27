"""
author:xiaoma
datetime:2019/12/26 13:38
describe:

"""
import allure
from params.parent_param_read_yaml import CreateHobbyMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("创建爱好")
class TestCreateHobbyMutation:

    @allure.title("创建爱好")
    def test_create_hobby_mutation(self):
        log.info("创建爱好")
        conf = Config()
        data = CreateHobbyMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('isSelected', str(res))