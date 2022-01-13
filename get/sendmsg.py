#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：sendmsg.py
@IDE  ：封装发送站内信消息的接口
@Author ：飞熊
@Date ：2021/12/15 7:29 下午 
"""
import logging

import requests
import uvicorn
from fastapi import FastAPI

from uids import uid_list
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()
pool = ThreadPoolExecutor()
body = {
    "account": "68349302",
    "type": "batch",
    "backup": 1,
    "content": "hello world",
    "uid": "20099490",
    "offline_push_desc": "",
    "ext": {

    },
    "srt": "sendmsg_accplay_01_01"
}

header = {
    "Content-Type": "application/json"
}


def send(uid: str, s_uid: str):
    body.update({'account': s_uid})
    result = requests.post(url='http://msg-dev.dz11.com/v3/api/message/syncsendmsg',
                           json=body,
                           headers=header)
    return result


@app.get("/sends")
def send_msg(uid: str):
    # 更新接收消息者uid
    body.update({'uid': uid})

    li = []
    for to_uid in uid_list:
        li.append((uid, to_uid))
    try:
        # 传参的格式为[(arg1,arg2),(arg1,arg2)]
        pool.map(lambda args: send(*args), li)
    except Exception as e:
        raise e

    return {"code": 0, "msg": "成功"}


if __name__ == '__main__':
    uvicorn.run(app='sendmsg:app', host='127.0.0.1', port=8000)
