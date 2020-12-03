# 位   置：南京邮电大学
# 程 序 员：邱礼翔
# 开发时间：2020/11/8 16:16
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('我的一个GUI程序')
root.geometry("500x300+100+200")

btn01=Button(root)      #创建按钮组件
btn02=Button(root)
btn01["text"]="点我送花"  #按钮上显示的文本信息
btn02["text"]="点我送草"

btn02.pack()     #把组件对象合理的放到窗口里面，顺序影响界面显示
btn01.pack()


def songhua(e):             # e就是事件对象
    messagebox.showinfo("Message","送你一朵玫瑰花，亲亲我吧")
    print("送你99朵玫瑰花")

def songcao(e):             # e就是事件对象
    messagebox.showinfo("Message","送你一个小草，绿绿你")
    messagebox.showinfo("Message", "送你二个小草，绿绿你")
    print("送你100个小草")

btn01.bind("<Button-1>",songhua)          #事件绑定
btn02.bind("<Button-1>",songcao)



root.mainloop()                  # 调用组件的mainloop() 方法，进入事件循环
