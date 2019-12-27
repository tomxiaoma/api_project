"""
author:xiaoma
datetime:2019/12/3 14:48
describe:

"""
import allure
from params.teacher_param_read_yaml import BoxesQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("教师端小红点")
class TestBoxesQuery:

    @allure.title("教师端小红点查询")
    def test_boxes_query(self):
        log.info("根据班级ID获取教师端小红点")
        conf = Config()
        data = BoxesQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('happenedAt', str(res))





