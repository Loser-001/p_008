#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/29 19:20

a=20
b=100  #两个整数类对象的相加操作
c=a+b
d=a.__add__(b)


print(c)
print(d)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
     return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2
print(s)
print('------------------------------------------')
lst=[11,22,33,44]
print(len(stu1))
print(lst.__len__())
print(stu1.__len__())