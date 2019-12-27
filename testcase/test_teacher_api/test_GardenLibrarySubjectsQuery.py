"""
author:xiaoma
datetime:2019/12/12 17:26
describe:

"""

import allure
from params.teacher_param_read_yaml import GardenLibrarySubjectsQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("园本库主题列表查询")
class TestGardenLibrarySubjectsQuery:

    @allure.title("园本库主题列表查询")
    def test_garden_library_subjects_query(self):
        log.info("园本库主题列表查询")
        conf = Config()
        data = GardenLibrarySubjectsQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('librarySubjects', str(res))