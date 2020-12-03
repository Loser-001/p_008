#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/27 16:07
def calc(a,b):
    c=a+b
    return c

d=calc(4,6)
print(d)

def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    print(odd)
    print(even)
    return odd,even

list1=[1,2,3,4,5,6,7,8,9,10]
print(fun(list1))

def fun1(*arges,**arges1):
    print(arges[1])
    print(arges1)
    return
def fun2(*arges2):
    print(arges2)
    return

def fun3(a,b,c):
    print('a=' ,a)
    print('b=',b)
    print('c=',c)
    return




print(fun1(12,13,35,a=14,b=98))
print(fun2(23,36))

lst3=[10,50,60]
fun3(*lst3)


print(10/0)

'''
import traceback
try:
    print('--------------------')
    print(1/0)
except :
      traceback.print_exc()
'''