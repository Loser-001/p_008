#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 17:06
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
class Teacher(Person):
      def __init__(self,name,age,teachofyear):
          super().__init__(name,age)
          self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()


