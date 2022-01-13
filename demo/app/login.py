#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：login.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/28 5:39 下午 
"""
from fastapi import APIRouter
from pydantic import BaseModel

from demo.app.register import di

router = APIRouter(tags=['login'])


class UserInfo(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(user: UserInfo):
    if user.username == di.get('name') and user.password == di.get('pwd'):
        return {'code': 0, "msg": 'success'}
    else:
        return {'code': 1001, "msg": '用户名或密码失败'}
