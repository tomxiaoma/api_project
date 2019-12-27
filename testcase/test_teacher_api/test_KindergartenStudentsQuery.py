"""
author:xiaoma
datetime:2019/12/13 10:56
describe:

"""

import allure
from params.teacher_param_read_yaml import KindergartenStudentsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据kindergarten_id查询该幼儿园所有学生")
class TestKindergartenStudentsQuery:

    @allure.title("根据kindergarten_id查询该幼儿园所有学生")
    def test_kindergarten_students_query(self):
        log.info("根据kindergarten_id查询该幼儿园所有学生")
        conf = Config()
        data = KindergartenStudentsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('students', str(res))
