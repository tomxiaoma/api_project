"""
封装Assert方法

"""
from common import Log
from common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_in(self, first_value, second_value):
        """
        :param first_value:
        :param second:
        :return:
        """
        try:
            assert first_value in second_value
            self.log.info("返回值中返回了对应的值! 需要找到关键词： %s, 实际返回结果 %s " % (first_value, second_value))
            return True
        except:
            self.log.error("返回值中没有找到对应的值, 预期结果需要找到关键词： %s, 实际返回结果 %s " % (first_value,second_value))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise


