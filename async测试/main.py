#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：main.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/27 3:48 下午 
"""
import asyncio
import time

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/get')
def get_time():
    start_time = time.time()
    time.sleep(1)  # fastapi 会将其放入thread pool 中执行
    end_time = time.time()
    print(f'all time is {end_time - start_time}')


@app.get('/get_async')
async def get_time():
    start_time = time.time()
    # await asyncio.sleep(1)
    time.sleep(1)  # 异步执行，但sleep为同步操作，会串行   导致阻塞
    end_time = time.time()
    print(f'all time is {end_time - start_time}')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000)
