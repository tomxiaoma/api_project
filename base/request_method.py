"""
# author:xiaoma
# datetime:2019/12/2 11:44
describe:涵盖http的请求方式
"""
import requests
import json
from common import Log


class RequestMethod:

    def __init__(self):
        self.log = Log.MyLog()

    def get_method(self,url,header,data=None):
        """
        封装get请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.get(url=url,data=data).json()
        else:
            res = requests.get(url=url,data=data,header=header).json()
        return res

    def post_method(self,url,data,header=None):
        """
        封装post请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,headers=header).json()
        return res

    def put_method(self,url,data,header=None):
        """
        封装put方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,header=header).json()
        return res

    def delete_method(self,url,data,header=None):
        """
        封装delete方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header == None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,header=header).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        """
        封装一个执行入口
        :param method:
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if method == 'post':
            res = self.post_method(url=url,data=data,header=header)
        elif method == 'get':
            res = self.get_method(url=url,data=data,header=header)
        elif method == 'put':
            res = self.put_method(url=url, data=data, header=header)
        elif method == 'delete':
            res = self.delete_method(url=url, data=data, header=header)
        else:
            self.log.error("暂时不支持其他请求方式")
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    re = RequestMethod()
    url = "http://teacher.kid17.com/auth/v1/teacher/auths/login"
    data = {"phone":"15900796431","password":"123123"}
    result = re.post_method(url=url,data=data,header=None)
    print(result)
