#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：register.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/28 5:39 下午 
"""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=['register'])


class UserInfo(BaseModel):
    username: str
    password: str


di = {}


# username为 6-10位
# password为 6-10位
@router.post('/register')
def register(user: UserInfo):
    username = user.username
    if username in di:
        return {'code': 0, 'msg': '用户已存在'}
    di[username] = user.password
    return {'code': 0, 'msg': '注册成功'}
