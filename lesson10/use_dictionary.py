# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/9 22:39

# Python字典特性：
# 1、无序性
# 2、可变的，可嵌套
# 3、键唯一
# 4、键不可变

dictionary = {'username': 'hanmeimei', 'age': 17, 'grade': '高一'}
print(dictionary)

# 创建空字典
empty_dict = {}
empty_dict = dict()

print(empty_dict)

# 通过映射函数创建字典
nba_stars_nickname = dict(zip(('邓肯', '吉诺比利', '帕克'), ('石佛', '妖刀', '跑车')))
print(nba_stars_nickname)
# zip(): 用于将多个列表或元组对应位置的元素组合为元组。返回的是这些内容的zip对象
nba_stars_list = list(zip(('邓肯', '吉诺比利', '帕克'), ('石佛', '妖刀', '跑车')))
print(nba_stars_list)

# 通过给定的关键字创建列表
family_members = dict(mama='妈妈', baba='爸爸', son='儿子', daughter='女儿')
print(family_members)

# 创建只有键-空值的字典
person_attr = ('username', 'age', 'sex')
person_dict = dict.fromkeys(person_attr)
print(person_dict)

# 用已经存在的列表或者元组创建字典
# 语法：dict = {tuple: list}
person_val = ['Jack', 20, 'Man']
person_dict = {person_attr: person_val}
print(person_dict)

# 删除字典，用del关键字
# del person_dict

# 清空字典：clear
# person_dict.clear()

# 删除元素：根据键
family_members.pop('mama')
print(family_members)

# 删除元素：根据值
print(family_members.popitem())
print(family_members)


# 字典的访问
print(dictionary['username'])

# 若访问的键不存在则会报错，因此需要判断
if 'age' in dictionary:
    print(dictionary['age'])

# Python中推荐使用get()方法访问字典
print(dictionary.get('username', 'unknown'))
print(dictionary.get('score', 'unknown'))

# 遍历字典
# items()返回键值对的元组
for item in dictionary.items():
    print(item)

for key, val in dictionary.items():
    print(key, ":", val)

print(dictionary.keys())
print(dictionary.values())

# 字典推导式

import random
randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
print('生成的字典是：', randomdict)
