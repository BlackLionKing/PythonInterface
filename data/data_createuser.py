def create_user_data():
    user_data = [('TestUser' + str(i), 'UserName' + str(i), [1], '137%08d' % i) for i in range(21, 30)]
    return user_data
