# coding=utf-8

# 2.2.2分片　

# 分片操作的实现需要提供两个索引作为边界,
# 第1个索引的元素是包含在分片内
# 第2个则不包含在分片内
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]  # 4, 5, 6
print numbers[0:1]  # 1
# 访问最后3个元素
print numbers[7:10]  # 7,8,9

# 负数的使用
print numbers[-3:-1]  # [8,9]

# 单个负数使用
print numbers[-3:]

# 单个整数使用
print numbers[:3]

# 代码清单 2_2 分片示例
# 对http://www.something.com形式的URL进行分割
# url = raw_input('Please enter the URL:')
# domain = url[11:-4]
# print 'Domain name:' + domain


# 步长的使用
# numbers[开始:结束:步长]
print numbers[0:10:1]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print numbers[0:10:2]  # [1, 3, 5, 7, 9]

print numbers[3:6:3]  # [4]

print numbers[::4]  # [1,5,9]

print numbers[8:3:-1]  # [9,8,7,6,5]

print numbers[5::-2]  # [6,4,2]

print numbers[:5:-2]  # [10,8]
