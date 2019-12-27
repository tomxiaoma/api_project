"""
author:xiaoma
datetime:2019/12/17 18:25
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteImageMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据照片ID删除已上传的照片")
class TestDeleteImageMutation:

    @allure.title("根据照片ID删除已上传的照片")
    def test_delete_image_mutation(self):
        log.info("根据照片ID删除已上传的照片")
        conf = Config()
        data = DeleteImageMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('rotation', str(res))
