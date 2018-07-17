#! python3
# encoding=utf-8
# @Time    : 2018/5/6 13:57
# @Author  : chaoswang
# @File    : TimerTest.py

import time
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(param):
    print(param, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

if __name__ == '__main__':
    sched = BlockingScheduler()
    # 因为my_job没参数，所以可以直接这样写，有参数的方法要在前面加“lambda:”，否则定时器会认为你传入的是一个函数调用的结果
    test = 'test'
    sched.add_job(lambda : my_job(test), 'interval', seconds=5)
    sched.start()
