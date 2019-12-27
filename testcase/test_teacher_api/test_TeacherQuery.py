"""
author:xiaoma
datetime:2019/12/16 17:20
describe:

"""
import allure
from params.teacher_param_read_yaml import TeacherQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据teacher_id查询教师信息")
class TestTeacherQuery:

    @allure.title("根据teacher_id查询教师信息")
    def test_teacher_query(self):
        log.info("根据teacher_id查询教师信息")
        conf = Config()
        data = TeacherQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('nickname', str(res))
