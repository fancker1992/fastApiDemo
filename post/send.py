#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastApiProject 
@File ：send.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2021/12/16 3:28 下午 
"""
from flask import Flask, request
import requests
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor()

app = Flask(__name__)

url = "http://msg-dev.dz11.com/v3/api/message/syncsendmsg"
uid_li = ['20050805', '20051045', '20103176', '20121703', '20125471', '23381640', '23381641', '23381642',
          '23381643',
          '26860640', '33571918', '39987101', '39987102', '41587831', '41587970', '43195864', '43196029',
          '44496401',
          '44496598', '44897741', '44897911', '44898020', '45298333', '45298349', '45298372', '45298373',
          '45298530',
          '45298531', '45898967', '45900114', '45901097', '46503232', '46503233', '46503271', '46504505',
          '46504536',
          '46504888', '46504889', '46504890', '46504891', '46504893', '46504895', '46504993', '50906825',
          '61008944',
          '64610826', '64612237', '64612238', '68345601', '68345645', '68345736', '68345755', '68346326',
          '68346358',
          '68346361', '68346362', '68346363', '68346376', '68346413', '68346414', '68346437', '68346440',
          '68346446',
          '68346452', '68346468', '68347117', '68347118', '68347120', '68347124', '68347138', '68347237',
          '68347273',
          '68347276', '68347277', '68347604', '68347618', '68347619', '68347622', '68347623', '68347624',
          '68347625',
          '68347633', '68347634', '68347691', '68347693', '68347695', '68347696', '68347697', '68347997',
          '68452771',
          '68452892', '68453171', '68853953', '68853954', '68853955', '68853956', '68853957', '68853958',
          '68853959',
          '68853960']


def hi_word():
    return '''
    许多新手玩家大多时间都过于谨慎和被动了，他们会在该下注(bet)时选择过牌(check)，在该加注(raise)时选择跟注(call)。
    当你有一副不错的手牌，如高对(AA, KK, QQ等)或者AK, AQ，你的打法应该更加具有攻击性。
    '''


def send_msg(f_uid, to_uid):
    payload = {
        "account": "{}".format(f_uid),
        "type": "batch",
        "backup": 1,
        "content": "{}".format(hi_word()),
        "uid": "{}".format(to_uid),
        "offline_push_desc": "",
        "ext":{},
        "srt": "sendmsg_accplay_01_01"
    }

    r = requests.post(url, json=payload)
    print(r.json())


@app.route('/')
def test():
    return {'code': 200, 'msg': 'success'}


@app.route('/send')
def send():
    li = []
    uid = request.args.get('uid')
    if not uid:
        return {'code': 200, 'msg': 'uid参数未传递'}

    for i in uid_li:
        li.append((i, uid))
    pool.map(lambda args: send_msg(*args), li)
    return {'code': 200, 'msg': 'send done'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6688)