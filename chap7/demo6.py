#位   置：南京邮电大学
#程 序 员：邱礼翔
#开发时间：2020/10/30 16:47

import schedule
import time

def job():
    print('哈哈---------------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

