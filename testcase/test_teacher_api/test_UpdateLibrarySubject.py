"""
author:xiaoma
datetime:2019/12/19 13:50
describe:

"""
import allure
from params.teacher_param_read_yaml import UpdateLibrarySubject
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
import pytest
from common import Log
log = Log.MyLog()


@allure.feature("编辑园本库主题")
class TestUpdateLibrarySubject:

    @pytest.mark.skip("暂时跳过test_update_library_subject（编辑园本库主题）测试")
    @allure.title("编辑园本库主题")
    def test_update_library_subject(self):
        log.info("编辑园本库主题")
        conf = Config()
        data = UpdateLibrarySubject().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('updateLibrarySubject', str(res))
