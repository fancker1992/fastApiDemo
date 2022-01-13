#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：main.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/28 5:41 下午 
"""
import uvicorn
from fastapi import FastAPI

from demo.app import login, register

app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8888)

