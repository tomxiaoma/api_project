"""
author:xiaoma
datetime:2019/12/18 16:25
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteLikeMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("老师取消点赞")
class TestDeleteLikeMutation:

    @allure.title("老师取消点赞")
    def test_delete_like_mutation(self):
        log.info("老师取消点赞")
        conf = Config()
        data = DeleteLikeMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('True', str(res))
