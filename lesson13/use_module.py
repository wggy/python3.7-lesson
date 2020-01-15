# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/14 0:12
# 模块的使用，简单来说，一个py文件就是一个文件

import sys

# import module: 导入模块，一个py文件
# from module import member : 导入模块中的成员，成员可以是类、函数或者变量


# 搜索模块目录，模块具体目录保存在sys.path
# 顺序：当前模块目录-->环境变量目录-->安装目录
print(sys.path)

# 有三种方式添加到sys.path

# 第一、临时添加
sys.path.append('G:/demo')
print(sys.path)


# 第二、添加.pth文件（推荐）
# 在安装目录中：C:\progms\Python36\Lib\site-packages，创建任意名称的.pth文件
# 添加导入目录：F:/test/demo

print(sys.path)

# 第三、在环境变量中添加，此处不表


