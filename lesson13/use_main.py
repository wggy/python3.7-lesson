# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/14 23:18

# 以主程序的形式执行
import lesson13.christmastree as tree

# 此时执行了所有函数体外部的代码，显然并不是我们想要的
print(tree.pinetree)

# 那么如何才能获取tree的变量呢？很简单，加个if判断即可
# if __name__ == '__main__'
# 此时执行模块tree，就是执行if块的语句

# 原理：每个模块中都保存了一个__name__变量，程序能识别该模块如何执行，
# 若自身运行，那么它的值就是__main__，如果被导入到其他模块中引用执行，那么久不是__main__


