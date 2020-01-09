# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/7 22:37

# Python使用循环结构
# for循环，语法：
# for var in obj:
#     循环体

# 例如：求1~100的和
sum = 0
for i in range(101):
    sum += i
print('1+...+100 = ', sum)

# range(start, end, step)
# start: 计数的起始值，可省略，默认为0
# end  ：计数的结束值，不包括该值，不可省略，range只有一个参数就是end
# step ：计数的步长，可省略，默认为1

# 遍历字符串
usage = '天道酬勤'
for ch in usage:
    print(ch)

# while循环
# while condition:
#     循环体

idx = 0
result = 0
while idx <= 100:
    result += idx
    print('result=', result)
    idx = idx + 1

print('今有物不知其数：三三数之剩二，五五数之声三，七七数之声二，问几何？')
none = True
number = 0
while none:
    number = number + 1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print('答曰：这个数是', number)
        none = False

# 跳转语句：continue、break
