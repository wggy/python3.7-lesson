# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/2 23:03

height = float(input('请输入你的身高（米）：'))
weight = float(input('请输入你的体重（公斤）：'))

bmi = weight / (height * height)

# 判断身高是否合理
if bmi < 18.5:
    print('BMI: ', bmi, '你的体重太轻了，多吃点肉')
elif bmi < 24.9:
    print('BMI: ', bmi, '你的体重正常，继续保持')
elif bmi < 29.9:
    print('BMI: ', bmi, '你的体重过重，要控制呀')
else:
    print('BMI: ', bmi, '你太肥了，要克制了')
