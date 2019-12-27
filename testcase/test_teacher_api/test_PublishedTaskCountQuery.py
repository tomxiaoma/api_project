"""
author:xiaoma
datetime:2019/12/13 11:43
describe:

"""
import allure
from params.teacher_param_read_yaml import PublishedTaskCountQuery
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common import Log
log = Log.MyLog()


@allure.feature("根据班级ID查询发布亲子任务总数")
class TestPublishedTaskCountQuery:

    @allure.title("根据班级ID查询发布亲子任务总数")
    def test_published_task_count_query(self):
        log.info("根据班级ID查询发布亲子任务总数")
        conf = Config()
        data = PublishedTaskCountQuery().yaml_data

        urls = data.url
        params = data.data
        headers = data.header
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_teacher + urls[0]
        res = RequestMethod().post_method(url=api_url, data=params[0], header=headers[0])
        assert Assertions().assert_in('publishedTasksCount', str(res))
