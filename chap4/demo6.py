#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/25 17:19
#输出一个三行四列的矩形
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()


