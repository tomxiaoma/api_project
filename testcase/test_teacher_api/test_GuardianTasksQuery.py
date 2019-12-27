"""
author:xiaoma
datetime:2019/12/13 10:55
describe:

"""
import allure
from params.teacher_param_read_yaml import GuardianTasksQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据teacherTaskID查询主题列表")
class TestGuardianTasksQuery:

    @allure.title("根据teacherTaskID查询主题列表")
    def test_guardian_tasks_query(self):
        log.info("根据teacherTaskID查询主题列表")
        conf = Config()
        data = GuardianTasksQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('nodes', str(res))
