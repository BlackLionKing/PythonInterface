import requests
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
        self.token = res['access_token']

    #
    # """
    #     读取成员接口
    # """
    # def get_user(self, userid, test_get_token):
    #     user_url = test_get_token[0] + f'/user/get?access_token={test_get_token[1]}&userid={userid}'
    #     response = requests.get(user_url)
    #     print(response.json())
    #     assert 'ok' == response.json()['errmsg']
    #
    # def create_user(self, userid, name, department, mobile, test_get_token):
    #     create_url = test_get_token[0] + f'/user/create?access_token={test_get_token[1]}'
    #     json_data = {
    #         'userid': userid,
    #         'name': name,
    #         'department': department,
    #         'mobile': mobile
    #     }
    #     response = requests.post(create_url, json=json_data)
    #
    # def update_user(self, userid, name, test_get_token):
    #     update_url = test_get_token[0] + f'/user/update?access_token={test_get_token[1]}'
    #     json_data = {
    #         "userid": userid,
    #         "name": name
    #     }
    #     response = requests.post(update_url, json=json_data)
    #     # 断言
    #     assert 'updated' == response.json()['errmsg']
    #
    # def delete(self, userid, test_get_token):
    #     delete_url = test_get_token[0] + f'/user/delete?access_token={test_get_token[1]}&userid={userid}'
    #     response = requests.get(delete_url)
    #     assert 'deleted' == response.json()['errmsg']
    #
    #
