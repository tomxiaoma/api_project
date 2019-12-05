"""
author:xiaoma
datetime:2019/10/21 11:20
describe:对json文件进行读取，并且根据对于的获取key的方法来拿到请求数据
"""
import json
import os
from common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class JSONReadUtil:

    def __init__(self, file_path=None):
        if file_path == None:
            log.error("无法找到文件")
        else:
            self.file_path = file_path
        self.data = self.read_json_data()

    def read_json_data(self):
        with open(self.file_path, encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    def get_key_data(self,key):
        """
        根据key获取数据
        :param key:
        :return:
        """
        return self.data[key]

if __name__ == "__main__":
    oper = JSONReadUtil()
    print(oper.get_key_data("appKey"))

