# coding=utf-8
# python包含6种内建的序列

edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print database

# 索引
greeting = 'Hello'  # 从0开始
print greeting[0]

print greeting[-1]  # 从后面提取

# fourth = raw_input('Year: ')[3]  # 2001
# print fourth  # 1  0开始

# 索引示例

# 据根给定的年月日以数字形式打印出日期
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 以1~31的数字作为续尾的列表
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']
print endings
# year = raw_input('year: ')
# month = raw_input('Month(1-12):')
# day = raw_input('Day(1-31):')

# month_number = int(month)
# day_number = int(day)

# 记得要将月分和天数减1,以获得正确的索引
# month_name = months[month_number - 1]
# ordinal = day + endings[day_number - 1]
#
# print month_name + ' ' + ordinal + '. ' + year
