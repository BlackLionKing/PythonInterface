import re

a = """
FAILED [ 50%]
test_chat_token.py:48 (Test_wx.test_creat_user[test7-\u54c8\u54c8\u54c8ha-department0-test5@gzdev.com])
'created' != 'userid existed, hint: [1647855490277971243988563], from ip: 1.119.196.78, more info at https://open.work.weixin.qq.com/devtool/query?e=60102'

Expected :'userid existed, hint: [1647855490277971243988563], from ip: 1.119.196.78, more info at https://open.work.weixin.qq.com/devtool/query?e=60102'
Actual   :'created'
<Click to see difference>

self = <test_chat_token.Test_wx object at 0x10d20f520>, userid = 'test7'
name = '哈哈哈ha', department = [1], email = 'test5@gzdev.com'
get_token = ('https://qyapi.weixin.qq.com/cgi-bin', 'gUju_3AtToCTOnyC3AIlzHB0GyeLXeMI2xKLyINJtyueeNC6786iGunQu3wUrJazC5B-neFLXrOmV...Js2pQ0y6Ml-YN-lEYSVyd-tkKuh0bfIjp0BkpQt43puNGuDvJYSpFPvMWNq7DadjGbYj21b3lxm_XmznYO6AEWnefpachyGOgbgzth3P6We_NDhSvJxvA')

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
>       assert 'created' == response.json()['errmsg']
E       AssertionError: assert 'created' == ('userid existed, hint: [1647855490277971243988563], from ip: 1.119.196.78, '\n 'more info at https://open.work.weixin.qq.com/devtool/query?e=60102')
E         - userid existed, hint: [1647855490277971243988563], from ip: 1.119.196.78, more info at https://open.work.weixin.qq.com/devtool/query?e=60102
E         + created

test_chat_token.py:60: AssertionError
"""

# pattern = re.compile(r'')
# 正则匹配
# print(re.findall(r"test7", a)[0])
# print(a)
