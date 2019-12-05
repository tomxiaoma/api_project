"""
author:xiaoma
datetime:2019/12/3 15:48
describe:
"""
from common.json_read import JSONReadUtil
import os
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class LoginToken:
    @staticmethod
    def get_teacher_token():
        read_json = JSONReadUtil(path_dir + '/params/token_teacher.json')
        token = read_json.get_key_data('token')
        user_id = read_json.get_key_data('user_id')
        request_header_data = {
            "X-User-Id": str(user_id),
            "Authorization": str(token)
        }
        return request_header_data

    @staticmethod
    def get_parent_token():
        read_json = JSONReadUtil(path_dir + '/params/token_parent.json')
        token = read_json.get_key_data('token')
        user_id = read_json.get_key_data('user_id')
        request_header_data = {
            "X-User-Id": str(user_id),
            "Authorization": str(token)
        }
        return request_header_data
