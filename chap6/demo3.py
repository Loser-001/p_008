#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 14:53
#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 14:34

class Student:
    native_place='吉林'
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def eat(self):
       #print('我的名字叫=',self.name,'年龄是=',self.age)
       print('学生在吃饭')
    @classmethod
    def cm(cls):
      print('我是类方法，因为我是用了classmethod进行了修饰')
def drink():
    print('喝水')
#创建Sstudent累的对象
stu1=Student('张三',20)
stu1.eat()
print(stu1.name)
print(stu1.age)
Student.eat(stu1)


'''
#创建Student类的对象
stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-----------------------------')
print(id(Student))
print(type(Student))
print(Student)
'''