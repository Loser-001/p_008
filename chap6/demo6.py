#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/28 16:31
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
       print('汽车已启动...')


car=Car('宝马X5')
car.start()
print(car.brand)