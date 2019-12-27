"""
author:xiaoma
datetime:2019/12/16 13:41
describe:

"""
import allure
from params.teacher_param_read_yaml import StudentsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据评价ID以及学生ID查询评估信息")
class TestStudentsQuery:

    @allure.title("根据评价ID以及学生ID查询评估信息")
    def test_students_query(self):
        log.info("根据评价ID以及学生ID查询评估信息")
        conf = Config()
        data = StudentsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('name', str(res))
