#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import werobot
import netease
import subprocess
import time
import urllib
import logging
import property
import myconst
import pyttsxtest
import sys
from werobot import client
from detect2imgs import detectBody

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)\

prop = property.parse('conf.prop')

robot = werobot.WeRoBot(token='tokenhere',enable_session=True)

wxclient = client.Client('wx49c0ee80455a9959','07b6943262c77b3dbdb18507492068ce')

@robot.subscribe
def subscribe(message):
    return myconst.subscribe_tips

@robot.text
def hello_world(message,session):
    content = message.content
    if content == 'aa':
        return myconst.aa_tips
    if content == 'tt':
        return [
            "微信你不懂爱",
            "龚琳娜最新力作",
            "http://weixin.com/budongai.mp3",
        ]
    if session.get('url') and content == '1':
        return [
            session.get('song_name'),
            session.get('artist'),
            session.get('url'),
        ]

    if 'aa ' in content:
        song_name = content.split('a ')[1]
        song_index = 0
        a = 0
        try:
            musicbox = netease.RasWxMusicbox(song_name)
            music_info = musicbox.get_music(song_index)
            mp3_url = music_info['mp3_url']
            while True:
                song_index = song_index + 1
                if song_index>10:
                    break
                if mp3_url == None:
                    music_info = musicbox.get_music(song_index)
                    mp3_url = music_info['mp3_url']
                else:
                    a = urllib.urlopen(mp3_url).getcode()
                    if a != 200:
                        continue
                    break
            if a != 200:
                return myconst.aa_unfind_tips
            song_info = u'正在播放:\n ' \
                        + u'演唱： ' + music_info['artist'] + '\n' \
                        + u'歌曲： ' + music_info['song_name']+ '\n' \
                        + u'回复：1 ： 返回歌曲'
            session["url"] = music_info['mp3_url']
            session["song_name"] = music_info['song_name']
            session["artist"] = music_info['artist']
            pyttsxtest.play('开始播放')
            play(mp3_url)
            return song_info
        except Exception,e:
            logger.error('search and play error', exc_info=True)
            return myconst.aa_error_tips

    if 'ab' == content:
        filepath = detectBody.detectBody.get_newest_img()
        #wxclient.upload_media('image',file(filepath))
        return detectBody.detectBody.snapshot_url

    if 'ac' == content:
        filepath = detectBody.detectBody.get_newest_img()
        #wxclient.upload_media('image',file(filepath))
        return detectBody.detectBody.stream_url

    if 'ad ' == content:
        tex = content.split('d ')[1]
        pyttsxtest.play(tex)
        return


    return myconst.all_func_tips



def play(mp3_url):
    try:
        subprocess.Popen(['pkill', 'mpg123'])
        time.sleep(.3)
    except:
        pass
    finally:
        subprocess.Popen(['mpg123', mp3_url])
        #        webbrowser.open(mp3_url)



robot.run(host='0.0.0.0',server='tornado',port=8082)
