"""
author:xiaoma
datetime:2019/12/16 17:08
describe:

"""
import allure
from params.teacher_param_read_yaml import LatestKindergartenLibraries
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("最新园本库列表查询")
class TestLatestKindergartenLibraries:

    @allure.title("最新园本库列表查询")
    def test_latest_Kindergarten_libraries(self):
        log.info("最新园本库列表查询")
        conf = Config()
        data = LatestKindergartenLibraries().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('latestKindergartenLibraries', str(res))
