#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import time
import pyttsxtest
from detect2imgs import detectBody


def run():
    while True:
        detectBody.detectBody.get_newest_img('../resources/imgs/newest.jpg')
        ff = detectBody.detectBody.compare_imgs()
        print ff
        if ff < 0.75:
            print 'beep'
            pyttsxtest.play('嘀嘀嘀')
        print 'no'
        time.sleep(3)

if __name__ == '__main__':
    run()