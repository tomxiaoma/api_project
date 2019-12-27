"""
author:xiaoma
datetime:2019/12/17 12:00
describe:

"""
import allure
from params.teacher_param_read_yaml import CreateTaskExampleSelectionMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("选用亲子任务库")
class TestCreateTaskExampleSelectionMutation:

    @allure.title("选用亲子任务库")
    def test_create_task_example_selection_mutation(self):
        log.info("选用亲子任务库")
        conf = Config()
        data = CreateTaskExampleSelectionMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('success', str(res))
