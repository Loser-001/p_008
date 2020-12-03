#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/11/8 14:52
for i in range(1,4):
    qq=input('请输入QQ号：')
    pwd=input('请输入密码：')
    if qq=='1669279462' and pwd =='1230':
        print('登陆成功')
        break
    else:
        print('账号或密码错误')
        if i<3:
            print(f'您还有{3-i}次机会')
else:
 print('循环已结束，三次机会已用完！！！！')