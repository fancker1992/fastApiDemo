#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：使用Query对参数进行额外的校验
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/15 4:03 下午 
"""
from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items")
def creat_item(q: Optional[str] = Query(None, min_length=3)):
    result = {"q": q}
    return result


# 将查询参数接受为list类型，每个元素必须为int类型   非必传
@app.get("/items2")
def read_item(q: Optional[List[int]] = Query(None)):
    result = {"q": q}
    return result


# 对查询参数通过Query设置默认值
@app.get("/items3")
def read_item(q: List[int] = Query([0, 0, 0])):
    result = {"q": q}
    return result


# 该list不对参数类型做校验
@app.get("/items4")
def read_item(q: list = Query([])):
    result = {"q": q}
    return result


if __name__ == '__main__':
    uvicorn.run(app='app', host="0.0.0.0", port=8001)

