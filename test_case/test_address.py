from api.address import Address


class Test_address(object):
    def setup(self):
        self.address = Address()

    def test_token(self):
        self.address.get_token()
