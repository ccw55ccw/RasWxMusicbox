#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import requests
import json
import urllib

def get_answer(tex):
    payload = {'token': 'B3224E6D44E79CF7D97104499A9C81C8', 'query': tex,'session_id':'0001'}
    r = requests.post("http://www.yige.ai/v1/query", data=payload)
    jsonobj = json.loads(r.text)
    return jsonobj['answer']

print urllib.quote('广州:12月6号 周二,11-20° 19° 多云 北风3-4级;大雪 周三,12-21° 多云 无持续风微风;12月8号 周四,13-22° 多云 无持续风微风;12月9号 周五,12-22° 晴 无持续风微风;')