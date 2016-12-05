#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import requests
import json

def get_answer(tex):
    payload = {'token': 'B3224E6D44E79CF7D97104499A9C81C8', 'query': tex,'session_id':'0001'}
    r = requests.post("http://www.yige.ai/v1/query", data=payload)
    jsonobj = json.loads(r.text)
    return jsonobj['answer']