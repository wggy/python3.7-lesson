# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/13 23:17

# 函数的使用

# 作业1：硬编码实现，匹配输出

def convertNum2Msg(num):
    """
    :param num: 输入代码
    :return: 返回信息
    """
    my_dict = {0: 'O', 1: 'I', 2: 'Z', 3: 'E', 4: 'Y', 5: 'S', 6: 'G', 7: 'L'}
    return my_dict.get(num)


print(convertNum2Msg(1))
print(convertNum2Msg(8))
