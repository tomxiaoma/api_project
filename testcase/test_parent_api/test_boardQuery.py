"""
author:xiaoma
datetime:2019/12/26 17:50
describe:

"""
import allure
from params.parent_param_read_yaml import BoardQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("通知详情查询")
class TestBoardQuery:

    @allure.title("通知详情查询")
    def test_board_query(self):
        log.info("通知详情查询")
        conf = Config()
        data = BoardQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('这是一条来自接口的请求', str(res))
