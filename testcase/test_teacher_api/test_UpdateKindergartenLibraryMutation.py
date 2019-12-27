"""
author:xiaoma
datetime:2019/12/19 13:44
describe:

"""

import allure
from params.teacher_param_read_yaml import UpdateKindergartenLibraryMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("园本库切换主题")
class TestUpdateKindergartenLibraryMutation:

    @allure.title("园本库切换主题")
    def test_update_kindergarten_library_mutation(self):
        log.info("园本库切换主题")
        conf = Config()
        data = UpdateKindergartenLibraryMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('updateKindergartenLibrary', str(res))
