#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 14:34

class Student:
    native_place='吉林'
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def info(self):
        print('我的名字叫=',self.name,'年龄是=',self.age)
    @classmethod
    def cm(cls):
      print('我是类方法，因为我是用了classmethod进行了修饰')
def drink():
    print('喝水')