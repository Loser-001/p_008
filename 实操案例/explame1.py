#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/11/8 14:19
'''使用print函数输出（输出目的地是文件）'''
fp=open('E:/test1.txt','a+')
print('风斗成就最好的你',file=fp)
fp.close()

'''第二种方式，使用文件读写操作'''
with open('E:/test2.txt','a+') as file:
    file.write('风斗成就最好的你')