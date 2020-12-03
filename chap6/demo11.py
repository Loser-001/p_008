#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 18:08
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')
class Cat(Animal):
    def eat(self):
        print('猫吃老鼠')


class Person(object):
       def eat(self):
           print('人吃五谷杂粮')
 #定义一个函数
def fun(a) :
    a.eat()

#开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('===================================')
fun(Person())

