#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import werobot
import netease
import subprocess
import time
import urllib

robot = werobot.WeRoBot(token='tokenhere',enable_session=True)

@robot.subscribe
def subscribe(message):
    return u'谢谢关注小五游侠订阅号！\n'+u'回复：a1->点歌台'+'\n'+u'其他功能敬请期待哈'




@robot.text
def hello_world(message,session):
    content = message.content
    if content == 'a1':
        return u"这是一个通过微信公众号点歌的一个webAPP（您点的歌曲也会在我家小音箱播放），发送：a1+歌曲名（搜索歌曲）"
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

    if 'a1+' in content:
        song_name = content.split('+')[1]
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
                return u'没找到这首歌。。。'
            song_info = u'正在我家的小音箱播放:\n ' \
                        + u'演唱： ' + music_info['artist'] + '\n' \
                        + u'歌曲： ' + music_info['song_name']+ '\n' \
                        + u'回复：1 ： 返回歌曲'
            session["url"] = music_info['mp3_url']
            session["song_name"] = music_info['song_name']
            session["artist"] = music_info['artist']
            play(mp3_url)
            return song_info
        except:
            return u'音乐搜索api出错，请换一首歌曲名称'

    return u'谢谢关注小五游侠订阅号！\n'+u'回复：a1->点歌台'+'\n'+u'其他功能敬请期待哈'



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
