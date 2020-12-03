#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 15:33

class Student:
    native_place='吉林'
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def eat(self):
       #print('我的名字叫=',self.name,'年龄是=',self.age)
       print('学生在吃饭')
    @staticmethod
    def method():
        print('我使用了staticemethod进行修饰，所以我是静态方法')
    @classmethod
    def cm(cls):
      print('我是类方法，因为我是用了classmethod进行了修饰')

#类属性的使用方式
print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)

print('-------类方法的使用方式--------')
Student.cm()
print('-------静态方法的使用方式--------')
Student.method()



'''      
def drink():
    print('喝水')
#创建Sstudent累的对象
stu1=Student('张三',20)
stu1.eat()
print(stu1.name)
print(stu1.age)
Student.eat(stu1)
'''

