# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/14 23:35

# 包的使用

# 包就是文件夹，用于管理py模块，不同的是包下会多个__init__.py
# 该文件是约定俗成的，同样也是一个模块文件，只不过模块名是包名
# __init__.py中可以写代码，在导入包后，其代码会自动执行

# 导入报的方式
# import pkg.module
# from pkg import module
# from pkg.module import member

# 引用其他模块
# 第三方模块的下载与安装使用pip