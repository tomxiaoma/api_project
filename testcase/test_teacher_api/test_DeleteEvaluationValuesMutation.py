"""
author:xiaoma
datetime:2019/12/17 18:17
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteEvaluationValuesMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("删除已评估的记录")
class TestDeleteEvaluationValuesMutation:

    @allure.title("删除已评估的记录")
    def test_delete_evaluation_values_mutation(self):
        log.info("删除已评估的记录")
        conf = Config()
        data = DeleteEvaluationValuesMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('deleteEvaluationValues', str(res))
