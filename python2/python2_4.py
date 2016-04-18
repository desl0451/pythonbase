# coding=utf-8

# 乘法
print 'python ' * 5  # python python python python python

print [42] * 10  # [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

print 42 * 10  # 420 乘法计算

sequence = [None] * 10
print sequence

# 序列(字符串) 乘法示例
# 以正确的宽度在居中的"盒子"内打印一个句子
# 注意,整数除法运算符(//)只能用在python 2.2

sentence = raw_input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print
print '' * left_margin + '+' + '-' * (box_width - 2) + '+'
print '' * left_margin + '|  ' + ' ' * text_width + '  |'
print '' * left_margin + '|  ' + sentence + '  |'
print '' * left_margin + '|  ' + ' ' * text_width + '  |'
print '' * left_margin + '+' + '-' * (box_width - 2) + '+'
