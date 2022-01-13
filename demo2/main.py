#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：多线程demo,线程数和系统cpu核数相同时，效率最高，最节省系统资源
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/31 7:53 下午 
"""
import os
import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b(t):
    time.sleep(t)
    print(f'sleeping...{t}...s')


executor = ThreadPoolExecutor(max_workers=os.cpu_count())
# b = executor.submit(wait_on_b, 0.1)

if __name__ == '__main__':
    # b.running()
    executor.map(wait_on_b, (2, 2, 2, 2, 2, 2, 2, 2, 4))
    print(os.cpu_count())
