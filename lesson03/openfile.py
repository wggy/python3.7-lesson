# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/2 22:40
import datetime

fd = open(r'demo.txt', 'a+')
print('要么出众，要么出局', file=fd)
fd.close()

print('当前年份：'+str(datetime.datetime.now().year))
print('当前日期：'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))