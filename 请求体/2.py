#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：请求体+路径参数+查询参数
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/15 3:07 下午 
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    age: int
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/{item_id}/")
def creat_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
        return result
