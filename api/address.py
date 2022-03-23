from string import Template

from api.base_api import BaseApi
from api.wework import Wework
import yaml


class Address(BaseApi):
    def __init__(self):
        # 初始化token信息 保证每次token只被执行一次
        corp_secret = "HYCEYvE8vImVbOK0DCtpryue_AksK28639bUtnrWDM4"
        wework = Wework()
        self.token = wework.get_token(corp_secret)
        # 初始化yaml文件
        with open('../data/requs.yaml') as f:
            # 使用模版语言读取yaml文件
            self.re = Template(f.read())

    """
        读取成员接口
    """
    def get_user(self, userid):
        # 定义yaml中变量的值
        value = {'userid': userid, 'access_token': self.token}
        # 将值传递给yaml文件
        params = self.re.safe_substitute(value)
        # 将yaml文件转换为python类型
        yaml_data = yaml.safe_load(params)
        # 发送请求
        response = self.send(yaml_data['requests'])
        print(response)

    def create_user(self, userid, name, department, mobile):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'params': {
                'access_token': self.token,
                'userid': {userid}
            },
            'json': {
                'userid': userid,
                'name': name,
                'department': department,
                'mobile': mobile
            }
        }
        response = self.send(data)
        print(response)

    def update_user(self, userid, name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            'params': {
                'access_token': self.token
            },
            'json': {
                "userid": userid,
                "name": name
            }
        }
        response = self.send(data)
        print(response)

    def delete_user(self, userid):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'params': {
                'access_token': self.token,
                'userid': userid
            }
        }
        response = self.send(data)
        print(response)
