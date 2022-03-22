# 创建用户 生成的数据
def create_user_data():
    user_data = [('TestUser' + str(i), 'UserName' + str(i), [1], '137%08d' % i) for i in range(11, 20)]
    return user_data


# 读取所有的userid
def read_user_data():
    user_data = create_user_data()
    print(user_data)
    user_name_list = []
    for i in user_data:
        # 切片 拿到userid
        user_name = i[0]
        user_name_list.append(user_name)
    return user_name_list


# list 包含 tuple 且 tuple内只有一个数据 会自带逗号 下面代码为去除逗号逻辑
"""
l = [1, 2, 3, 5, 4]
l1 = []
l2 = []
for i in l:
    l1.append(i)
    print(l1)
    t = tuple(l1)
    l2.append(t)
    print(l2)
    l1 = []
l2 = [(1,), (2,), (3,), (5,), (4,)]
print('[' + ', '.join('({})'.format(t[0]) for t in l2) + ']')
"""
