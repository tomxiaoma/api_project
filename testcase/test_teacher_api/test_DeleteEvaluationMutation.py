"""
author:xiaoma
datetime:2019/12/17 17:56
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteEvaluationMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据发展评估ID删除整条评估")
class TestDeleteEvaluationMutation:

    @allure.title("根据发展评估ID删除整条评估")
    def test_delete_evaluation_mutation(self):
        log.info("根据发展评估ID删除整条评估")
        conf = Config()
        data = DeleteEvaluationMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('EvaluationInfo', str(res))
