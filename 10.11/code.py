#1.下面程序的功能是从键盘读入一个球的半径（单位为米），计算并输出其体积和表面积，
#要求计算结果保留2 位小数。程序运行后的输入输出情况如下图所示。
#请在横线处填写适当的语句或表达式将程序补充完整
'''
from math import *
r=input("r=")
r=float(r)
v=(4/3)*pi*r**3
s=4*pi*r**2
print("v={0:.2f}m^3,s={1:.2f}m^2".format(v,s))
'''
#2.下面程序的功能是从键盘读入一个整数，将其依次转换为二进制、八进制、十进制和十六进制数输出。
#请在横线处填写适当的语句或表达式将程序补充完整。
'''
x=input('x=')
x=int(x)
print('0bx={0:b},0ox={0:o},x={0:d},0xx={0:x},'.format(x))
'''
#3.下面程序的功能是从键盘读入一个英文字符串，分别输出其中UTF-8 编码最大和最小的那个英文字母。
'''
x=input("x=")
x=list(x)
m=max(x)
n=min(x)
print("maxChar={},minChar={}".format(m,n))
'''
#5.下面程序的功能是从键盘读入一个英文字符串，分别输出其中UTF-8 编码最大和最小的那个英文字母。
'''
x=input("x=")
x=list(x)
m=max(x)
n=min(x)
print("maxChar={},minChar={}".format(m,n))
'''
#5.下面程序的功能是从键盘读入任意多个整数，输出这些数及其和。要求不使用循环语句。
'''
x=input('x=')
x=eval(x)
print(x)
s=sum(x)
print('sum={}'.format(s))
'''
#6.下面程序的功能是从键盘读入三角形的三个边长（单位为米），输出其周长和面积。
'''
from math import *
a,b,c=eval(input('a,b,c='))
t=(a+b+c)/2
s=sqrt(t*(t-a)*(t-b)*(t-c))
print('length={:.4f}m,area={:.4f}m^2'.format(2*t,s))
'''
#7. 下面程序的功能是 下面程序的功能是 下面程序的功能是从键盘读入一个任意字符串,输出其字符个数。
'''
s=input('s=')
n=len(s)
print('n={}'.format(n))
'''
#8. 下面程序的功能是从键盘读一个复数，分别输出其实部 、虚部、模
'''
from cmath import *
c=eval(input('c='))
r=c.real
i=c.imag
m=abs(c)
print('real={},imag={},abs={}'.format(r,i,m))
'''
#9. 居中显示单词
'''
s=input('s=')
print('{:^20}'.format(s))
'''
#10.菱形
'''
s='***********************'
print('{:^11.1s}'.format(s))
print('{:^11.3s}'.format(s))
print('{:^11.5s}'.format(s))
print('{:^11.7s}'.format(s))
print('{:^11.9s}'.format(s))
print('{:^11.11s}\n{:^11.9s}\n{:^11.7s}\n{:^11.5s}\n{:^11.3s}\n{:^11.1s}'.format(s,s,s,s,s,s))
'''
#11. 用井号替换上一题的空格
'''
s='***********************'
t='#######################'
print('{0:#^11.1s}'.format(s,t))
print('{0:#^11.3s}'.format(s))
print('{0:#^11.5s}'.format(s))
print('{0:#^11.7s}'.format(s))
print('{0:#^11.9s}'.format(s))
print('{0:#^11.11s}'.format(s))
'''
#12.最大最小值
'''
a,b,c,d=eval(input('a,b,c,d='))
m=max(a,b,c,d)
n=min(a,b,c,d)
print('max={},min={}'.format(m,n))
'''
#13. 画个M
'''
s='***********************'
print('{0:>7.1s}{0:7.7s}{0:>8.8s}{0:>20.8s}{0:>8.8s}'.format(s))
print('{0:>7.2s}{0:7.6s}{0:>9.8s}{0:>18.8s}{0:>10.8s}'.format(s))
print('{0:>7.3s}{0:7.5s}{0:>10.8s}{0:>16.8s}{0:>12.8s}'.format(s))
print('{0:>7.4s}{0:7.4s}{0:>11.8s}{0:>14.8s}{0:>14.8s}'.format(s))
print('{0:>7.5s}{0:7.3s}{0:>12.8s}{0:>12.8s}{0:>16.8s}'.format(s))
print('{0:>7.6s}{0:7.2s}{0:>13.8s}{0:>10.8s}{0:>18.8s}'.format(s))
print('{0:>7.7s}{0:7.1s}{0:>14.8s}{0:>8.8s}{0:>20.8s}'.format(s))
'''
# 14. W
'''
s='***********************'
print('{0:>7.7s}{0:7.1s}{0:>14.8s}{0:>8.8s}{0:>20.8s}'.format(s))
print('{0:>7.6s}{0:7.2s}{0:>13.8s}{0:>10.8s}{0:>18.8s}'.format(s))
print('{0:>7.5s}{0:7.3s}{0:>12.8s}{0:>12.8s}{0:>16.8s}'.format(s))
print('{0:>7.4s}{0:7.4s}{0:>11.8s}{0:>14.8s}{0:>14.8s}'.format(s))
print('{0:>7.3s}{0:7.5s}{0:>10.8s}{0:>16.8s}{0:>12.8s}'.format(s))
print('{0:>7.2s}{0:7.6s}{0:>9.8s}{0:>18.8s}{0:>10.8s}'.format(s))
print('{0:>7.1s}{0:7.7s}{0:>8.8s}{0:>20.8s}{0:>8.8s}'.format(s))
'''
#15.下面程序的功能是从键盘读入一批 整数使用这些创建一个列表输出该列表 输出该列表 ，再 输出该 列表 的元素个数首尾元素。
'''
x=eval(input('x='))
x=list(x)
n=len(x)
print('x={}'.format(x))
print('numX={},leftX={},rightX={}'.format(n,x[0],x[-1]))
'''
#16.略
#17
'''
d={}
name=input('name=')
score=eval(input('score='))
d[name]=score
name=input('name=')
score=eval(input('score='))
d[name]=score
name=input('name=')
score=eval(input('score='))
d[name]=score
name=input('name=')
score=eval(input('score='))
d[name]=score
print('dict={}'.format(d))
print('numDict={}'.format(len(d)))
'''
#18
'''
dict={'张一': 92, '张二': 95, '张三': 88, '张四': 90}
print('{}:{}'.format('你可以查询下同学的成绩',list(dict.keys())))
name=input('name=')
print('{}的成绩是{}'.format(name,dict[name]))
'''
#19
'''
x=eval(input('x='))
s=set(x)
num=len(s)
m=max(s)
n=min(s)
print('set={},numSet={}'.format(s,num))
print('maxSet={},minSet={}'.format(m,n))
'''
#20
'''
s={2,4,7,5,9,3,6,8}
x=int(input('x='))
b=x in s
print('{}在集合中为：{}'.format(x,b))
print('set={}'.format(s))
'''
x=int(input('x='))
print('x={0:d},{0:b}'.format(x))
y=x^15
print('y={0:d},{0:b}'.format(y))
