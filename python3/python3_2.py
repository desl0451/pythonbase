# coding=utf-8

# 2.3.2 基本的列表操作
# 1.改变列表: 元素赋值
x = [1, 1, 1]
x[1] = 2
print x

# 2.删除元素
names = ['Alice', 'Beth', 'Cecil']
del names[2]
print names

# 3.分片赋值
name = list('Perl')
print name  # ['P', 'e', 'r', 'l']
name[2:] = list('ar')
print name  # ['P', 'e', 'a', 'r']

# 将下标1后面的内容替失为ython
name = list('Perl')
name[1:] = list('ython')
print name  # ['P', 'y', 't', 'h', 'o', 'n']

# 插入新数据
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers  # [1, 2, 3, 4, 5]

# 替换为空
numbers[1:4] = []
print numbers
