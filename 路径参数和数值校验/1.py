#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：1.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/15 5:28 下午 
"""
from fastapi import FastAPI, Path

app = FastAPI()
"""
gt：大于（greater than）
ge：大于等于（greater than or equal）
lt：小于（less than）
le：小于等于（less than or equal）"""


# 路径参数可以通过Path进行限制
@app.get("/items/{item_id}")
async def read_items(

        q: str,
        item_id: int = Path(..., ge=2, title="The ID of the item to get")

):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
