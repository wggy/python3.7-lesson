# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/5 22:39

# 正则表达式的使用
# 使用match()方法匹配，如果匹配成功则返回Match对象，否则返回None
# 语法：re.match(pattern, string, [flags])
# flags：可选参数，表示标志位，控制匹配方式，如是否区分字母大小写等

import re

pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern, string, re.I)
print(match)
print('匹配的起始位置：' + str(match.start()))
print('匹配的截止位置：' + str(match.end()))
print('匹配位置的元组：' + str(match.span()))
print('要匹配的字符串：' + match.string)
print('匹配数据：' + match.group())


# search()：用于检索第一个匹配的字符串
# 语法：re.search(pattern, string, [flags])

# findall(): 匹配符合所有条件的字符串，并以列表的形式返回，如果匹配成功，则返回列表，否则，返回None

match = re.findall(pattern, string, re.I)
print(match)

string = 'dilidi MR_SHOP mr_shop'
match = re.match(pattern, string, re.I)
print(match)

# sub()：替换字符串
# re.sub(pattern, repl, string, [count], [flags])
pattern = r'1[3|4|5|7|8]\d{9}'
string = '中将号码为：8371232， 联系电话为：13822321111'
print(re.sub(pattern, '1XXXXXXXX', string))

# split()：使用正则表达式分割字符串，返回的是列表
# re.split(pattern, string, [maxsplit], [flags])
pattern = r'[?|&]'
url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=c0f369ef0049dbdd&ie=utf-8'
print(re.split(pattern, url))
