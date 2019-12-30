"""
author:xiaoma
datetime:2019/12/19 14:48
describe:

"""
import os
from params import tools
from common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPagesParent.get_page_list()
    param = data[name]
    return param


class YamlData:
    def __init__(self,params):
        self.url = []
        self.data = []
        self.header = []
        self.yaml_input(params)

    def yaml_input(self,params):
        for i in range(0, len(params)):
            self.url.append(params[i]['url'])
            self.data.append(params[i]['data'])
            self.header.append(params[i]['header'])


class Login:
    """
    登录读取yaml文件
    """
    def __init__(self):
        params = get_parameter('Login')
        self.yaml_data = YamlData(params=params)


