"""
author:xiaoma
datetime:2019/12/17 15:44
describe:

"""
import allure
from params.teacher_param_read_yaml import CreateTeacherTaskMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("创建亲子任务")
class TestCreateTeacherTaskMutation:

    @allure.title("创建亲子任务")
    def test_create_teacher_task_mutation(self):
        log.info("创建亲子任务")
        conf = Config()
        data = CreateTeacherTaskMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('createdTeacherTask', str(res))
