# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/7 22:21
# if分支的使用

# if condition:
#    do()
# elif condition:
#    do()
# else:
#    do()

# 如果if语句后只有一条语句可放一行
age = int(input("请输入你的年龄："))
if age > 18: print('你成年了')
else: print('你是未成年')

# if else 简写
data = -1
# if data > 0:
#     copy = data
# else:
#     copy = -data


# 简写程成：
copy = data if data>0 else -data
print("copy: ", copy)

# 使用not关键字表示否定，and表示与关系，or表示或关系
data = None
if not data:
    print('you lost')
else:
    print('you win')

# Python中False，None，空列表，空字符串，空字段，空元组在逻辑判断中都相当与False
