"""
author:xiaoma
datetime:2019/12/19 13:31
describe:

"""
import allure
from params.teacher_param_read_yaml import UpdateEvaluationFinishedMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("完成发展评估")
class TestUpdateEvaluationFinishedMutation:

    @allure.title("完成发展评估")
    def test_update_evaluation_finished_mutation(self):
        log.info("完成发展评估")
        conf = Config()
        data = UpdateEvaluationFinishedMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('True', str(res))
