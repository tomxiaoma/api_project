"""
author:xiaoma
datetime:2019/12/17 10:34
describe:

"""
import allure
from params.teacher_param_read_yaml import CreateActivity
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("创建在园时光")
class TestCreateActivity:

    @allure.title("创建在园时光")
    def test_create_activity(self):
        log.info("放入园本库")
        conf = Config()
        data = CreateActivity().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('createdTeacherActivity', str(res))