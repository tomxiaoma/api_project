"""
author:xiaoma
datetime:2019/12/16 17:13
describe:

"""
import allure
from params.teacher_param_read_yaml import LibraryGradesQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("园本库年级列表查询")
class TestLibraryGradesQuery:

    @allure.title("园本库年级列表查询")
    def test_library_grades_query(self):
        log.info("园本库年级列表查询")
        conf = Config()
        data = LibraryGradesQuery().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken().get_teacher_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('librarySubjects', str(res))
