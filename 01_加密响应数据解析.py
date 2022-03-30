import json

import requests
import base64


def decode():
    # 本地服务 返回一串base64加密的数据
    url = 'http://127.0.0.1:8090/test_1.txt'
    response = requests.get(url)
    # base64.b64decode(response.content) 解密返回的二进制数据
    # json.loads() 将字符串转为字典
    decode_res = json.loads(base64.b64decode(response.content))

    print(decode_res)


decode()
