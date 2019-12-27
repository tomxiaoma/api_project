"""
author:xiaoma
datetime:2019/12/6 16:33
describe:

"""
import allure
from params.teacher_param_read_yaml import ClazzFeedListQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据clazz_id分页查询家庭时光列表查询")
class TestClazzFeedListQuery:

    @allure.title("根据clazz_id分页查询家庭时光列表查询")
    def test_clazz_feedList_query(self):
        log.info("根据clazz_id分页查询家庭时光列表查询")
        conf = Config()
        data = ClazzFeedListQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('id', str(res))





