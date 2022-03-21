import json
import re

import pytest
import requests


class Test_wx(object):

    """
        获取token
        token失效时间2h
        不宜多次请求token接口 只在类中运行一次
    """
    @pytest.fixture(scope='session')
    def get_token(self):
        # 接口
        url = 'https://qyapi.weixin.qq.com/cgi-bin'
        token_url = url + '/gettoken'
        # 参数
        params = {
                    "corpid": "wwc4fcb20970b14103",
                    "corpsecret": "HYCEYvE8vImVbOK0DCtpryue_AksK28639bUtnrWDM4"
        }
        # 拿到token
        response = requests.get(token_url, params=params)
        token = response.json()['access_token']

        return url, token

    """
        读取成员接口
    """
    @pytest.mark.parametrize('userid', [('BaiTianMing')])
    @pytest.mark.skip
    def test_getuser(self, userid, get_token):
        user_url = get_token[0] + f'/user/get?access_token={get_token[1]}&userid={userid}'
        response = requests.get(user_url)
        assert '白天明' == response.json()['name']

    """
        创建成员
            发送数据必须为json格式
        requests.post()
            data参数传的dict类型
            json参数传的json类型

    """
    # @pytest.mark.skip
    @pytest.mark.parametrize('userid, name, department, email', [('test7', '哈哈哈ha', [1], 'test5@gzdev.com')])
    def test_creat_user(self, userid, name, department, email, get_token):
        create_url = get_token[0] + f'/user/create?access_token={get_token[1]}'
        json_data = {
            'userid': userid,
            'name': name,
            'department': department,
            'email': email
        }
        response = requests.post(create_url, json=json_data)
        # 断言
        try:
            assert 'created' == response.json()['errmsg']
        # 异常处理
        except AssertionError as e:
            # 保存信息中如果有userid existed
            if 'userid existed' in e.__str__():
                print('userid已存在')

    """
        修改成员

    """
    @pytest.mark.skip
    @pytest.mark.parametrize('userid, name', [('test7', '一一一')])
    def test_update_user(self, userid, name, get_token):
        update_url = get_token[0] + f'/user/update?access_token={get_token[1]}'
        json_data = {
            "userid": userid,
            "name": name
        }
        response = requests.post(update_url, json=json_data)
        # 断言
        assert 'updated' == response.json()['errmsg']

    """
        删除成员

    """
    @pytest.mark.parametrize('userid', [('test7')])
    @pytest.mark.skip
    def test_delete(self, userid, get_token):
        delete_url = get_token[0] + f'/user/delete?access_token={get_token[1]}&userid={userid}'
        response = requests.get(delete_url)
        assert 'deleted' == response.json()['errmsg']


if __name__ == '__main__':
    pytest.main(['-vs'])
