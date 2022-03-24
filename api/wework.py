from string import Template

import yaml

from api.base_api import BaseApi


class Wework(BaseApi):
    def __init__(self):
        with open('../data/requests_data.yaml') as f:
            self.re = Template(f.read())

    def get_token(self, corp_secret):
        value = {'corpsecret': corp_secret}
        params = self.re.safe_substitute(value)
        yaml_data = yaml.safe_load(params)
        # 发送请求
        token = self.send(yaml_data['get_token']['requests'])
        token_data = token['access_token']
        return token_data
