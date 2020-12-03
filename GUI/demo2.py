# 位   置：南京邮电大学
# 程 序 员：邱礼翔
# 开发时间：2020/11/8 16:48
"""测试一个经典的GUI程序的写法，使用面向对象的方式"""
from tkinter import *
from tkinter import messagebox
class Application(Frame):
   """一个经典的GUI程序的类写法"""
   def __init__(self,master=None):
       super().__init__(master)  #super() 代表父类的定义，而不是父类对象
       self.master=master
       self.pack()
       
       pass
       self.createwidget()

   def createwidget(self):
      """创建组件"""
      self.btn01 = Button(self)
      self.btn01["text"] = "点我送花"
      self.btn01.pack()
      self.btn01["command"]=self.songhua
      #创建一个·退出按钮
      self.btnQuit =Button(self,text="退出",command=root.destroy)

   def songhua(self):
        messagebox.showinfo("送花","送你99朵玫瑰花")
        print('"送你99朵玫瑰花"')
        self.btnQuit.pack()
root = Tk()
root.geometry("400x100+200+300")
root.title("一个经典的程序类测试")
app = Application(master=root)
root.mainloop()