#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/29 18:57

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建C类对象
x=C('Jack',20)
print(x.__dict__)   #实例对象的属性字典
print(C.__dict__)
print('-------------------------------')
print(x.__class__)  #输出了对象所属的类
print(C.__bases__)  #C类的父类的元组
print(C.__base__)
print(C.__mro__)  #累的层次结构
print(A.__subclasses__())
