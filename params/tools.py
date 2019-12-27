"""
读取yaml测试数据

"""

import yaml
import os
import os.path

def open_teacherapi():
    """
    打开教师api接口请求文件
    :return:
    """
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/params/Param/teacherapi'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r',encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages

def open_parentapi():
    """
        打开家长api接口请求文件
        :return:
        """
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/params/Param/parentapi'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r',encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPagesTeacher:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = open_teacherapi()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


class GetPagesParent:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = open_parentapi()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
