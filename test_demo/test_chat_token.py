import pytest
import requests
from test_demo.create_user import create_user_data, read_user_data
from filelock import FileLock


class Test_wx(object):

    """
        获取token
        token失效时间2h
        不宜多次请求token接口 只在类中运行一次
    """
    @pytest.fixture(scope='session')
    def test_get_token(self):
        token = None
        # 接口
        url = ''
        # 文件锁 防止xdist并行 执行多次该方法
        with FileLock("./test_demo/session.lock"):
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
    @pytest.mark.parametrize('userid', read_user_data())
    # @pytest.mark.skip
    def test_getuser(self, userid, test_get_token):
        user_url = test_get_token[0] + f'/user/get?access_token={test_get_token[1]}&userid={userid}'
        response = requests.get(user_url)
        print(response.json())
        assert 'ok' == response.json()['errmsg']

    """
        创建成员
            发送数据必须为json格式
        requests.post()
            data参数传的dict类型
            json参数传的json类型

    """
    @pytest.mark.skip
    @pytest.mark.parametrize('userid, name, department, mobile', create_user_data())
    def test_creat_user(self, userid, name, department, mobile, test_get_token):
        create_url = test_get_token[0] + f'/user/create?access_token={test_get_token[1]}'
        json_data = {
            'userid': userid,
            'name': name,
            'department': department,
            'mobile': mobile
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
    def test_update_user(self, userid, name, test_get_token):
        update_url = test_get_token[0] + f'/user/update?access_token={test_get_token[1]}'
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
    def test_delete(self, userid, test_get_token):
        delete_url = test_get_token[0] + f'/user/delete?access_token={test_get_token[1]}&userid={userid}'
        response = requests.get(delete_url)
        assert 'deleted' == response.json()['errmsg']


if __name__ == '__main__':
    pytest.main(['-vs'])
