#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project ：fastApiProject 
@File ：1.py
@IDE  ：请求体+路径参数
@Author ：飞熊
@Date ：2021/12/14 9:00 下午 
"""

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
