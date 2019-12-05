"""
author:xiaoma
datetime:2019/10/28 13:50
describe:操作登录响应的token信息，拿到响应数据并使用一个json文件存起来，方便后面使用鉴权的接口调用
"""
import json
import os
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class HeaderUtil:
    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_data(self):
        """
        根据登录返回的信息，依据响应只拿取data部分
        :return:
        """
        return self.response['data']

    def get_request_header(self):
        """
        拿到请求使用的数据
        :return:
        """
        return self.get_response_data()

    def write_teacher_header(self):
        """
        拿到响应的登录数据并写入token_teacher.json文件中
        :return:
        """
        res_data = dict(self.get_request_header())
        with open(path_dir + '/params/token_teacher.json', 'w') as fp:
            fp.write(json.dumps(res_data))

    def write_parent_header(self):
        """
        拿到响应的登录数据并写入token_parent.json文件中
        :return:
        """
        res_data = dict(self.get_request_header())
        with open(path_dir + '/params/token_parent.json', 'w') as fp:
            fp.write(json.dumps(res_data))




