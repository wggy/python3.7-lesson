# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/14 23:45

# 文件操作
# file = open(filename, mode, buffering)
# filename: 文件名称
# mode: 打开文件模式
# buffering: 是否开启缓存，0：不开启，1：开启，大于1：缓冲区大小，默认开启缓存

# file = open('test.txt', 'a+', encoding='utf-8')
# file.write("黑发不知读书早，白首方知读书迟")
# file.close()

# 读取全部
with open('test.txt', 'r', encoding='utf-8') as file:
    str = file.read()
    print(str)

# 逐行读取
with open('test.txt', 'r', encoding='utf-8') as file:
    num = 0
    while True:
        num = num + 1
        line = file.readline()
        if line == '':
            break
        print(num, line, '\n')

# 读取全部行
with open('test.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())