"""
author:xiaoma
datetime:2019/12/18 14:55
describe:

"""

import allure
from params.teacher_param_read_yaml import DeleteKindergartenLibraryMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据内容ID删除园本库内容")
class TestDeleteKindergartenLibraryMutation:

    @allure.title("根据内容ID删除园本库内容")
    def test_delete_kindergarten_library_mutation(self):
        log.info("根据内容ID删除园本库内容")
        conf = Config()
        data = DeleteKindergartenLibraryMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('deleteKindergartenLibrary', str(res))