import pytest

from api.address import Address
from data.data_createuser import create_user_data


class Test_address(object):
    def setup(self):
        self.address = Address()

    def test_get_user(self):
        self.address.get_user('BaiTianMing')

    @pytest.mark.parametrize('userid, name, department, mobile', create_user_data())
    def test_create_user(self, userid, name, department, mobile):
        self.address.create_user(userid, name, department, mobile)

    def test_update_user(self):
        self.address.update_user('909090', 'xx')

    def test_delete_user(self):
        self.address.delete_user('909090')


if __name__ == '__main__':
    pytest.main(['-v s'])
