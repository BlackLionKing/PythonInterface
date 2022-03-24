import pytest
import yaml
from api.address import Address
from data.data_createuser import create_user_data


class Test_address(object):
    def setup(self):
        self.address = Address()
        # 加载yaml文件
        self.data = yaml.safe_load(open('../data/params_data.yaml'))

    def test_get_user(self):
        self.address.get_user(self.data['get_user'])

    @pytest.mark.parametrize('userid, name, department, mobile', create_user_data())
    def test_create_user(self, userid, name, department, mobile):
        self.address.create_user(userid, name, department, mobile)

    def test_update_user(self):
        self.address.update_user(self.data['update_user'][0], self.data['update_user'][1])

    def test_delete_user(self):
        self.address.delete_user(self.data['delete_user'])


if __name__ == '__main__':
    pytest.main(['-v s'])
