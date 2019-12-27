"""
author:xiaoma
datetime:2019/12/19 11:38
describe:

"""
import allure
from params.teacher_param_read_yaml import MarkGuardianTasksMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("将亲子任务标记为已读")
class TestMarkGuardianTasksMutation:

    @allure.title("将亲子任务标记为已读")
    def test_mark_guardian_tasks_mutation(self):
        log.info("将亲子任务标记为已读")
        conf = Config()
        data = MarkGuardianTasksMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher+ urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('True', str(res))
