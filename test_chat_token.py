import json

import pytest
import requests


class Test_wx(object):

    """
        获取token
        token失效时间2h
        不宜多次请求token接口 只在类中运行一次
    """
    def setup_class(self):
        # 接口
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        # 参数
        params = {
                    "corpid": "wwc4fcb20970b14103",
                    "corpsecret": "HYCEYvE8vImVbOK0DCtpryue_AksK28639bUtnrWDM4"
        }
        # 拿到token
        response = requests.get(url, params=params)
        self.token = response.json()['access_token']

    """
        读取成员接口
    """
    def test_getuser(self):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
                'access_token': self.token,
                'userid': 'BaiTianMing'
        }
        response = requests.get(url, params=params)
        print(response.json())

    """
        创建成员
            发送数据必须为json格式
        requests.post()
            data参数传的dict类型
            json参数传的json类型 
                
    """
    def test_creat_user(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params = {
            "access_token": self.token,
            # 调试参数
            # "debug": 1
        }

        response = requests.post(url, params=params, json=json.load(open('./create_user.json', 'r')))
        print(response.json())


if __name__ == '__main__':
    pytest.main(['-vs'])
