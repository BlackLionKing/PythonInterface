from api.base_api import BaseApi


class Wework(BaseApi):
    def get_token(self, corp_secret):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                "corpid": "wwc4fcb20970b14103",
                "corpsecret": corp_secret
            }
        }
        # 拿到token
        res = self.send(data)
        token = res['access_token']
        return token
