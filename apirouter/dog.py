#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：dog.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/28 4:27 下午 
"""
from fastapi import APIRouter

router = APIRouter(tags=['dog'])


@router.get('/get_name_dog')
def get_name():
    return {'name': 'i am dog'}


@router.get('/get_voice_dog')
def get_voice():
    return {'voice': '汪汪~'}
