"""
author:xiaoma
datetime:2019/12/26 13:47
describe:

"""
import allure
import pytest
from params.parent_param_read_yaml import DeleteCollectionMutation
from config.config import Config
from base.request_method import RequestMethod
from common.Assert import Assertions
from common.login_toke import LoginToken
from common import Log
log = Log.MyLog()


@allure.feature("家长取消放入成长册")
class TestDeleteCollectionMutation:

    @pytest.mark.skip("暂时停止test_delete_collection_mutation（家长取消放入成长册）测试")
    @allure.title("家长取消放入成长册")
    def test_delete_collection_mutation(self):
        log.info("家长取消放入成长册")
        conf = Config()
        data = DeleteCollectionMutation().yaml_data

        urls = data.url
        params = data.data
        headers = LoginToken.get_parent_token()
        log.info("请求头信息：" + str(headers))
        log.info("请求体信息：" + str(params[0]))
        api_url = conf.host_parent + urls[0]
        res= RequestMethod().post_method(url=api_url, data=params[0], header=headers)
        assert Assertions().assert_in('', str(res))
