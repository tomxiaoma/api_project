"""
author:xiaoma
datetime:2019/12/19 11:18
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteTeacherTaskMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("老师删除亲子任务")
class TestDeleteTeacherTaskMutation:

    @allure.title("老师删除亲子任务")
    def test_delete_teacher_task_mutation(self):
        log.info("老师删除亲子任务")
        conf = Config()
        data = DeleteTeacherTaskMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('deletedTeacherTask', str(res))