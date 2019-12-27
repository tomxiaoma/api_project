"""
author:xiaoma
datetime:2019/12/27 11:03
describe:

"""
import allure
from params.parent_param_read_yaml import PlatformNotificationDetail
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("七七说消息详情查询")
class TestPlatformNotificationDetail:

    @allure.title("七七说消息详情查询")
    def test_platform_notification_detail(self):
        log.info("七七说消息详情查询")
        conf = Config()
        data = PlatformNotificationDetail().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('createdAt', str(res))
