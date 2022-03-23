from api.base_api import BaseApi


class Address(BaseApi):
    def get_token(self):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                "corpid": "wwc4fcb20970b14103",
                "corpsecret": "HYCEYvE8vImVbOK0DCtpryue_AksK28639bUtnrWDM4"
            }
        }
        # 拿到token
        res = self.send(data)
        token = res['access_token']
        return token

    """
        读取成员接口
    """
    def get_user(self, userid):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'params': {
                'access_token': self.get_token(),
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
                'access_token': self.get_token(),
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
                'access_token': self.get_token()
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
                'access_token': self.get_token(),
                'userid': userid
            }
        }
        response = self.send(data)
        print(response)
