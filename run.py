#coding=utf-8
import time
import itchat
import netease
import threading
import os
import subprocess
import webbrowser
import signal
import yigeai

itchat.auto_login()
will_play_list = []
process = None


def musicbox():
    @itchat.msg_register
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            #return 'I received: %s'%msg.get('Content', '')
            content = msg.get('Content', '')
            return yigeai.get_answer(content)
    itchat.run()


def play(mp3_url):
    try:
        subprocess.Popen(['pkill', 'mpg123'])
        time.sleep(.3)
    except:
        pass
    finally:
        subprocess.Popen(['mpg123', mp3_url])
#        webbrowser.open(mp3_url)

if __name__ == '__main__':
    musicbox()

