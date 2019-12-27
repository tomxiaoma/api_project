"""
author:xiaoma
datetime:2019/12/26 10:57
describe:

"""
import allure
from params.parent_param_read_yaml import CreateChildFeed
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("家长创建个人动态")
class TestCreateChildFeed:

    @allure.title("家长创建个人动态")
    def test_create_child_feed(self):
        log.info("家长创建个人动态")
        conf = Config()
        data = CreateChildFeed().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('API数据', str(res))
