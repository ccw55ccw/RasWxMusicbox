#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import werobot
import netease
import subprocess
import time

robot = werobot.WeRoBot(token='tokenhere')

@robot.text
def hello_world(message):
    content = message.content
    help(message)
    content_list = content.split()
    if len(content_list) == 1:
        song_name = content
        musicbox = netease.RasWxMusicbox(song_name)
        music_list = musicbox.gen_music_list()
        return music_list
    if len(content_list) == 2:
        try:
            song_name = content_list[0]
            song_index = int(content_list[1])
            musicbox = netease.RasWxMusicbox(song_name)
            music_info = musicbox.get_music(song_index)
            mp3_url = music_info['mp3_url']
            song_info = u'正在播放:\n ' \
                        + u'专辑： ' + music_info['album_name'] + '\n' \
                        + u'演唱： ' + music_info['artist'] + '\n' \
                        + u'歌曲： ' + music_info['song_name']
            play(mp3_url)
            return song_info
        except:
            return u'输入有误，请重新输入'
    else:
        return u'输入有误，请重新输入'
    return 'Hello World!'

def play(mp3_url):
    try:
        subprocess.Popen(['pkill', 'mpg123'])
        time.sleep(.3)
    except:
        pass
    finally:
        subprocess.Popen(['mpg123', mp3_url])
#        webbrowser.open(mp3_url)

robot.run(host='0.0.0.0',server='tornado')
