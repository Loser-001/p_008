#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/11/8 15:21
import random
price=random.randint(1000,1500)
print('今日竞猜的商品为小米扫地机器人：‘价格在1000--1500之间’')


while True:
     guess=int(input('请输入商品价格：'))
     if guess>price:
        print('大了,请重新猜','商品价格为：{}'.format(price))
     elif guess<price:
        print('小了,请重新猜','商品价格为：{}'.format(price))
     elif guess == price :
        print('你猜对了')
        break


