"""
author:xiaoma
datetime:2019/12/17 17:34
describe:

"""
import allure
from params.teacher_param_read_yaml import DeleteTeacherCommentMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()
import pytest


@allure.feature("老师删除评论")
class TestDeleteTeacherCommentMutation:

    @allure.title("老师删除评论")
    def test_delete_teacher_comment_mutation(self):
        log.info("老师删除评论")
        conf = Config()
        data = DeleteTeacherCommentMutation().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('deleteComment', str(res))
