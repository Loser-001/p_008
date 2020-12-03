#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/25 16:09
'''
for item in 'python':
    print(item)


for i in range(10):
    pass
print(i)

for _ in range(5):
    print('人生苦短，我用python')
sum=0
for j in range(1,101):
    if j%2==0:
        sum=sum+j
print(sum)
'''

a=135
print(int(a/100))
print(int(a/10%10))
print(a%10)
'''输出a100到999之间的水仙花数'''
s=0
for i in range(100,1000):
    a=int(i/100) #百位
    b=int(i/10%10)  #十位
    c=int(i%10)  #个位
    if i==a**3+b**3+c**3:
        print(i)
        s=1
if s==0:
  print('当中没有水仙花数')





