# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/9 23:11

# 集合：保存不重复元素的容器
# 1、可变集合：set
# 2、不可变结合：frozenset

# 创建集合：set1 = {ele1, ele2, ele3}
# 使用set()方法创建集合
# 语法：setname = set(iteration)
# iteration: 科技转变为集合的可迭代对象：列表、元组、range对象等，也可以是字符串，返回的是不重复的字符集合
set1 = set('我思故我在')
print(set1)
set2 = set([1, 2, 3, 4])
print(set2)
set3 = set(('人生苦短', '我用Python'))
print(set3)

# 创建空集合智能用set()
emptyset = set()

# 向集合中添加元素
# setname.add(element)
# element: 只能是字符串，元组，布尔值等不可变对象，不能是字典、列表等可变对象
set1.add('.')
print(set1)

# 删除集合：del setname
# 删除元素：
# 删除值：setname.remove('1')
# 删除最后一个元素：setname.pop()
set1.pop()
print(set1)

# 集合的交集：&
# 集合的并集：|
# 集合的差集：-
set1 = set([1, 2, 3])
set2 = set([3, 4, 5, 6])
print('set1 & set2: ', set1 & set2)
print('set1 | set2: ', set1 | set2)
print('set1 - set2: ', set1 - set2)
