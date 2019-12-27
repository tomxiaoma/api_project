"""
author:xiaoma
datetime:2019/12/13 10:56
describe:

"""

import allure
from params.teacher_param_read_yaml import LibrarySubjectQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据园本库ID查询园本库主题")
class TestLibrarySubjectQuery:

    @allure.title("根据园本库ID查询园本库主题")
    def test_library_subject_query(self):
        log.info("根据园本库ID查询园本库主题")
        conf = Config()
        data = LibrarySubjectQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('semesterStatus', str(res))
