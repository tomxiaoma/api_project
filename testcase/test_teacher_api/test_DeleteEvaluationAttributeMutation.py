"""
author:xiaoma
datetime:2019/12/17 17:41
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteEvaluationAttributeMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("删除单个发展评估主题")
class TestDeleteEvaluationAttributeMutation:

    @allure.title("删除单个发展评估主题")
    def test_delete_evaluation_attribute_mutation(self):
        log.info("删除单个发展评估主题")
        conf = Config()
        data = DeleteEvaluationAttributeMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('EvaluationInfo', str(res))
