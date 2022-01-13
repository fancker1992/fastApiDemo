#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiDemo
@File ：main.py
@IDE  ：PyCharm
@Author ：飞熊
@Date ：2021/12/12 1:38 下午
"""
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, p: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p": p}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# if __name__ == '__main__':
#     uvicorn.run(app='main:app', host="0.0.0.0", port=8001)
