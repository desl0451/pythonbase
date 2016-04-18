# coding=utf-8

# 2.2.5成员资格 检查一个值是否在序列中
# permissions = 'rw'
# print 'w' in permissions
#
# print 'x' in permissions
#
# users = ['mlh', 'foo', 'bar']
# print raw_input('Enter your user name: ') in users
#
# print '################################'
# print '$$$ Get rich now!!! $$$'
# subject = '$$$ Get rich now!!! $$$'
# print '$$$' in subject

# 代码清单2-4 序列成员资格示例
# 检查用户名和PIN码
# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7524'],
#     ['jones', '9843']
# ]
#
# username = raw_input('User name:')
# pin = raw_input('PIN code:')
# if [username, pin] in database:
#     print 'Access granted'


# 2.2.6 长度、最小值和最大值
# 内建函数len,min 和max
numbers = [100, 34, 678]
print '序列数量'
print len(numbers)
print '数列最大值'
print max(numbers)
print '数列最小值'
print min(numbers)

print '求指定数列最大值'
print max(2, 3)

print '求指定数列最小值'
print min(9, 3, 2, 5)
