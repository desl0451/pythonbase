# coding=utf-8

# 2.3.3 列表方法
# lst = [1, 2, 3]
# lst.append(4)
# print lst  # [1, 2, 3, 4]

# 2.count 统计某个元素在列表中出现的次数

# print ['to', 'be', 'or', 'not', 'to', 'be'].count('to')  # 2
# x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
#
# print x.count(1)  # 2
#
# print x.count([1, 2])  # 1

# 3.extend 方法可以在列表的末尾一次性追加另一个序列的多个值
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print a  # [1, 2, 3, 4, 5, 6]

# 4.index 方法用于从列表中找出某个值第一个匹配项的索引位置
# knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
# print knights.index('who')
# print knights.index('swho') #没有找到会出现异常

# 5.insert 方法用于将对象插入到列表中
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.insert(3, 'four')
# print numbers  # [1, 2, 3, 'four', 4, 5, 6, 7]

# 6.pop 方法会移除列表中的一个元素(默认是最后一个元素)
# 并且返回元素的值
# x = [1, 2, 3]
# print x.pop()
# print x.pop(0)
# print x

# 7.remove 方法用于移除列表中某个值的第一个匹配项
# x = ['to', 'be', 'or', 'not', 'to', 'be']
# x.remove('be')
# print x

# 8.reverse 方法将列表中的元素反向存放
# x = [1, 2, 3]
# x.reverse()
# print x

# 9.sort方法用于在原位置
x = [4, 6, 2, 1, 7, 9]
x.sort()
print x
