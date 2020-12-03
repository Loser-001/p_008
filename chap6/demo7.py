#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 16:36

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希在类的外部使用，所以加了两个下划线
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',30)
stu.show()

#在类的外部使用name与age
print(stu.name)
#print(stu.__age)

print(dir(stu))
print(stu._Student__age) #在类的外部可以通过_Student__age(加下划 线）使用


