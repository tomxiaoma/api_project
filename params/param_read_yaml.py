
"""
定义所有测试数据

"""
import os
from params import tools
from common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
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
    def __init__(self):
        params = get_parameter('Login')
        self.yaml_data = YamlData(params=params)


class ActivityExampleQuery:
    def __init__(self):
        params = get_parameter('ActivityExampleQuery')
        self.yaml_data = YamlData(params=params)


class BoxesQuery:
    def __init__(self):
        params = get_parameter('BoxesQuery')
        self.yaml_data = YamlData(params=params)


class UseActivityExampleLogMutation:
    def __init__(self):
        params = get_parameter('UseActivityExampleLogMutation')
        self.yaml_data = YamlData(params=params)


class ClazzFeedListQuery:
    def __init__(self):
        params = get_parameter('ClazzFeedListQuery')
        self.yaml_data = YamlData(params=params)


class ClazzStudentsQuery:
    def __init__(self):
        params = get_parameter('ClazzStudentsQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationAttributeQuery:
    def __init__(self):
        params = get_parameter('EvaluationAttributeQuery')
        self.yaml_data = YamlData(params=params)

class EvaluationDetailQuery:
    def __init__(self):
        params = get_parameter('EvaluationDetailQuery')
        self.yaml_data = YamlData(params=params)