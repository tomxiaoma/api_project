"""
author:xiaoma
datetime:2019/12/18 16:16
describe:根据内容ID删除园本库内容

"""

import allure
import pytest
from params.teacher_param_read_yaml import DeleteLibrarySubject
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("根据主题ID删除园本库主题")
class TestDeleteLibrarySubject:

    @pytest.mark.skip("跳过测试TestDeleteLibrarySubject（根据主题ID删除园本库主题）")
    @allure.title("根据主题ID删除园本库主题")
    def test_delete_library_subject(self):
        log.info("根据主题ID删除园本库主题")
        conf = Config()
        data = DeleteLibrarySubject().yaml_data

        req_url = conf.host_debug
        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = req_url + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('', str(res))
