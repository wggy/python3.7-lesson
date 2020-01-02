# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/2 22:45

import datetime

username = input('请输入姓名：')
# python3.7中input输入的信息都是字符类型
bornyear = int(input('请输入出生年份：'))

print('姓名：', username, '，出生：', bornyear)

nowyear = datetime.datetime.now().year

age = nowyear - bornyear

if age > 65:
    print(username, '你是老年人了，辛苦一生，希望你晚年幸福')
elif age > 18:
    print(username, '，你是成年人啦！恭喜你将要养活自己不被饿死直到65岁')
else:
    print(username, '你未成年，可能还是个宝宝')


