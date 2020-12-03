#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/25 16:44

for i  in range(3):
    pwd=input('请输入密码：')
    if pwd == '888':
       print('密码正确')
       break
    else:
        print('密码不正确')
if i==2:
  print('密码超出限制')


'''
i=0
while i<=2:
    pwd=input('请输入密码：')
    if pwd == '888':
        break
    else:
        print('密码不正确')
        i = i + 1
if i==3:
   print('输入超出限制')
else:
    print('密码正确')

'''
