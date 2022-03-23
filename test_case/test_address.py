import pytest

from api.address import Address


class Test_address(object):
    def setup(self):
        self.address = Address()

    def test_get_user(self):
        self.address.get_user('BaiTianMing')

    def test_create_user(self):
        self.address.create_user('909090', 'xxxx', [1], '18201535343')

    def test_update_user(self):
        self.address.update_user('909090', 'xx')

    def test_delete_user(self):
        self.address.delete_user('909090')


if __name__ == '__main__':
    pytest.main(['-v s'])
