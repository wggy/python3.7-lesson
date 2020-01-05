# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/5 21:47

# 字符串拼接：+
# 注意：字符串不允许其他类型的数据拼接
age = 18
username = 'James'
print(username + ': ' + str(age))

# 获取字符串长度
pymsg = '\n\r\b人生苦短；我用Python；再用Shell；最后用 Java\t\r\n'
print(len(pymsg))

# 字符串截取
# string[start: end: step]
print(pymsg[:4])

# 字符串分割：split
# 语法：str.split(sep, maxsplit)
# sep: 分隔符，默认为None，表示所有空字符，包含空格、换行符、制表符等
# maxsplit：可选参数，用于指定分割的次数，不指定或者指定为-1表示分割次数没有限制

print(pymsg.split())
print(pymsg.split('；'))
print(pymsg.split('；', 1))

# 检索字符串
# count(): 用于检索指定字符串在另一个字符串中出现的次数
# str.count(sub, start, end)
print(pymsg.count('；'))
print(pymsg.count('；', 0, 6))

# find()：用于检索是否包含指定的字符串，如果包含返回字符串第一次出现的位置，否则返回-1
# str.find(sub, start, end)
print(pymsg.find('Java'))
print(pymsg.find('Golang'))

# 如果只想判断字符串是否存在，用in
print('Shell' in pymsg)

# rfing()：查找从右向左查
print(pymsg.rfind('Java'))

# index(): 同find()方法类似，区别是index方法没有查到子字符串会报错
# 同样的还有rindex()方法
# print(pymsg.index('Golang'))

# startswith()： 检测字符串是否以指定的子字符串开头
print(pymsg.startswith('1人生'))

# endswith()：检测字符串是否以指定的子字符串结尾
print(pymsg.endswith('Java'))

# 字符串大小写转换
print(pymsg.upper())
print(pymsg.lower())

# 去除字符串中的特殊字符
# strip()：去掉左右两侧的特殊字符
# str.strip([chars])
# chars: 去掉指定的特殊字符
# lstrip()：去掉左侧的特殊字符
# rstrip()：去掉右侧的特殊字符
print('-------------------')
print(pymsg.strip('\n'))
print(pymsg.strip('\n'))

# 格式化字符串：
# 使用%占位符
template = '编号：%09d\t公司名称：%s\t官网：https://www.%s.com'
baidu = (1, '百度', 'baidu')
taobao = (2, '淘宝', 'taobao')
print(template%baidu)
print(template%taobao)

# 从python2.6开始，提供了format方法格式化
# str.format(args)
# str：用于规定字符串显示的模板，args：用于指定替换的项

template = '编号：{:0>9s}\t公司名称：{:s}\t官网：https://www.{:s}.com'
print(template.format('3', '知乎', 'zhihu'))
print(template.format('4', '腾讯', 'qq'))