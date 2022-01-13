#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：cat.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/28 4:25 下午 
"""
from fastapi import APIRouter

router = APIRouter(prefix='/cat', tags=['cat'])


@router.get('/get_name_cat')
def get_name():
    return {"name": 'i am cat'}


@router.get('/get_voice_cat')
def get_voice():
    return {'voice': '喵喵~'}
