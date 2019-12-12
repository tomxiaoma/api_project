"""
author:xiaoma
datetime:2019/12/6 16:42
describe:

"""
import allure
from params.param_read_yaml import ClazzStudentsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据班级ID查询所在班级的所有学生")
class TestBoxesQuery:

    @allure.title("查询所有学生")
    def test_test_boxes_query(self):
        log.info("查询所有学生")
        conf = Config()
        data = ClazzStudentsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_debug + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('students', str(res))