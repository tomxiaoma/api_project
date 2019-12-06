"""
author:xiaoma
datetime:2019/12/6 16:33
describe:

"""
import allure
from params.param_read_yaml import ClazzFeedListQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Assert
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()

@allure.feature("根据clazz_id分页查询家庭时光列表查询")
class TestBoxesQuery:

    @allure.title("根据clazz_id分页查询家庭时光列表查询")
    def test_test_boxes_query(self):
        log.info("根据clazz_id分页查询家庭时光列表查询")
        conf = Config()
        data = ClazzFeedListQuery().yaml_data

        req_url = conf.host_debug
        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = req_url + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        log.info("返回结果："+str(res))
        assert Assertions().assert_in('id', str(res))





