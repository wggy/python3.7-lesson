# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/4 19:51

# python中序列是最基本的数据结构、它是一块用于存储多个值的连续内存结构
# python中内置了5个基本的数据结构：
# 1、列表
# 2、元组
# 3、集合
# 4、字典
# 5、字符串

# 索引，正向索引从0开始，反向索引从最后一个开始，用-1表示，逐渐递减，倒一个元素位置是-1，倒二元素就是-2

# 序列
verse = ['圣安东尼奥马刺', '达拉斯小牛', '休斯敦火箭', '金州勇士']
print(verse[2])
print(verse[-1])

# 切片
# 序列的切片操作用来访问指定范围内的元素
# 访问语法：sname[start : end : step]
# sname：切片名称
# start: 切片开始的位置，包括该位置，如不指定，默认是0
# end  ：切片结束的位置，不包括该位置，如不指定，则默认为序列的长度
# step : 切片的步长，如省略，默认为1

nbastars = ['迈克尔乔丹', '科比布莱恩特', '麦克格雷迪', '姚明', '斯蒂芬库里', '勒布朗詹姆斯']

print(nbastars[1:4:2])
print(nbastars[1:3])

# 拷贝序列
copynbastars = nbastars[::]
copynbastars.append('易建联')
print(copynbastars)
print(nbastars)

# 序列相加：将两个序列连接，相同数据类型的序列就可以连接，且忽略数据类型，不同数据类型不支持
nbawifes = ['金卡戴珊', '可乐卡戴珊', '瓦妮莎']
print(nbastars + nbawifes)
nbaages = [18, 30, 38]
print(nbastars + nbawifes + nbaages)

# 如：数组+字符串序列就会报错：TypeError: can only concatenate list (not "str") to list
# print(nbaages + "nba球员年龄阶段")

# 乘法
# python中一个序列*数字n=新的序列，新的序列为原序列重复n次，序列乘法必须为正整数，否则报错
print(nbaages * 3)

# 序列乘法有个常用功能是创建指定长度的空序列
emptylist = [None] * 5
print(emptylist)

# in : 判断序列包含元素；反之not in表示不包含关系
print('姚明' in nbastars)
print('凯文杜兰特' not in nbastars)

# 序列长度、最大值、最小值：len(sname)，max(sname)，min(sname)
print(len(nbastars))
print(max(nbastars))
print(min(nbastars))

# 列表的其他内置函数：
# 1、list()：将序列转为列表
# 2、str() ：将序列转为字符串
# 3、sum() ：对序列求和
# 4、sorted()：序列排序
# 5、reversed()：反向排列序列元素
# 6、enumerate()：将序列组合为一个索引序列，多用在for虚幻中
print(sum(nbastars))