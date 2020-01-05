# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/4 21:12

# 元组: 不可变序列，t = (ele1, ele2, ...)

womanStars = ('迪丽热巴', '娜扎', '杨幂', '徐冬冬', '柳岩')

# 使用type()函数查看变量的类型
print(type(womanStars))

emptytuple = ()

# 元素不支持增加、删除和修改元素

# range创建元组
numtuple = tuple(range(0, 20, 3))
print(numtuple)

# 元组推导式，同列表推导式

number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number = tuple(number)
print(number)