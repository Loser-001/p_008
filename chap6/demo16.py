#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/29 20:32

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
#(2)类有浅拷贝
print('---------------------------')
disk=Disk() #创建一个硬盘类对象
computer=Computer(cpu1,disk)
#浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#
