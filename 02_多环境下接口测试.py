import requests
import yaml


def send():
    yaml_data = yaml.safe_load(open('./env.yaml'))
    # 通过default的值 来判断测试环境
    req_url = yaml_data['url_dict'][yaml_data['url_dict']['default']] + 'test_1.txt'
    # 发送请求
    res = requests.request(yaml_data['method'], req_url)
    print(res.text)


send()
