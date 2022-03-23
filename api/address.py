from api.base_api import BaseApi
from api.wework import Wework


class Address(BaseApi):
    # 初始化token信息 保证每次token只被执行一次
    def __init__(self):
        corp_secret = "HYCEYvE8vImVbOK0DCtpryue_AksK28639bUtnrWDM4"
        wework = Wework()
        self.token = wework.get_token(corp_secret)

    """
        读取成员接口
    """
    def get_user(self, userid):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'params': {
                'access_token': self.token,
                'userid': {userid}
            }
        }
        response = self.send(data)
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
