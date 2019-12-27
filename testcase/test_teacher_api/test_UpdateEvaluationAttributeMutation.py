"""
author:xiaoma
datetime:2019/12/19 11:26
describe:

"""
import allure
from params.teacher_param_read_yaml import UpdateEvaluationAttributeMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("编辑单条发展评估")
class TestUpdateEvaluationAttributeMutation:

    @allure.title("编辑单条发展评估")
    def test_teacher_tasks_query(self):
        log.info("编辑单条发展评估")
        conf = Config()
        data = UpdateEvaluationAttributeMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('evaluationCategoryId', str(res))
