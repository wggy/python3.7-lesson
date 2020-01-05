# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/4 20:26
# 列表：listname = [ele1, ele2, ele3,...]，列表支持嵌套，虽然列表支持多种数据类型
# 通常为了程序的可读性，一个列表只放一种数据类型

emptylist = []

# list()将range()范围函数转为列表
numlist = list(range(10, 20, 2))
print(numlist)

# del：删除列表，del关键字并不常用，因为python自带垃圾回收功能
del emptylist

# 遍历列表
# 1、for循环
for item in numlist:
    print(item)

# 2、for循环和enumerate()函数，支持访问索引序列
for index, item in enumerate(numlist):
    print(index + 1, item)

# 元素操作：增删改
# 列表增加：append在末尾添加
numlist.append(100)
print(numlist)

# insert函数支持在列表指定位置添加元素，但效率不如append高
numlist.insert(1, 9999)
print(numlist)

# extend()函数支持向列表中添加一个列表，功能同列表相加+，区别呢？未知？
numlist2 = list(range(1, 10, 2))
print(numlist2)
numlist.extend(numlist2)
print(numlist)


# 修改元素
numlist[0] = 'updated'
print(numlist)

# 删除元素
# 1、根据索引删除
del numlist[0]
print(numlist)
# 2、根据取值删除，若删除不存在的元素，程序报错中断（但是笔者没发现报错，程序是中断了）
# numlist.remove('sfdsd')
# print(numlist)

# 3、删除前，先判断是否存在，count用于判断元素出现的次数，次数为0，则表示元素不存在
numlist[0] = 'test'
print(numlist)
if numlist.count('test') > 0 :
    numlist.remove('test')
print(numlist)

# 统计元素出现的次数
print(numlist.count(12))

# 获取元素的下标索引
print(numlist.index(18))

# 统计元素之和
print(sum(numlist))

# 列表元素排序：使用内置函数sorted和使用列表函数sort()
# sort()： listname.sort(key=None, reverse=True)，默认是升序
# 另外sort()排序对中文支持不友好，如需使用，要改写相应代码
print(sorted(numlist))
numlist.sort(key=None, reverse=True)
print(numlist)

# sorted()：sorted(listname, key=None, reverse=False)
# 列表的这两种方法功能基本相同，所不同的是sort()会改变元素的顺序
# sorted()并不会改变元素的顺序，而是建立一个副本存储排序的结果

# 列表推导式
# 格式1：list = [ Expr for in range ]
# 格式2：newlist = [ Expr for var in list]
# 格式3：newlist = [ Expr for var in list if condition ]



