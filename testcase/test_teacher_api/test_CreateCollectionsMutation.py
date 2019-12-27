"""
author:xiaoma
datetime:2019/12/17 11:07
describe:

"""
import allure
from params.teacher_param_read_yaml import CreateCollectionsMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("教师放入成长册")
class TestCreateCollectionsMutation:

    @allure.title("教师放入成长册")
    def test_create_collections_mutation(self):
        log.info("教师放入成长册")
        conf = Config()
        data = CreateCollectionsMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('rotation', str(res))