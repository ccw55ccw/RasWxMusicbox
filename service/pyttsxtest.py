# encoding=utf-8

import urllib
import urllib2
import json
import pygame
import time
import subprocess

## get access token by api key & secret key

def get_token():
    apiKey = "VGytExSCNlNG5v8lYnf3qC2G"
    secretKey = "66a04380543440cf778417416a040122"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

#24.15ff145dd6c623e9efa6cae142170c5a.2592000.1483444628.282335-8779558
#24.e78c9feb6ded277f644bc9f1da926c40.2592000.1483444662.282335-8779558

def play(tex):
    token = '24.e78c9feb6ded277f644bc9f1da926c40.2592000.1483444662.282335-8779558'
    url = 'http://tsn.baidu.com/text2audio?tex='+tex+'&tok='+token+'&ctp=1&cuid=4545&lan=zh'
    # data = urllib.urlopen(url).read()
    # filepath = 'tt'+str(time.time())+'.mp3'
    # f = file(filepath, 'wb')
    # f.write(data)
    # f.close()
    # pygame.mixer.init()
    # track = pygame.mixer.music.load(filepath)
    # pygame.mixer.music.play()
    subprocess.Popen(["mpg123", url])
    time.sleep(2)

if __name__ == "__main__":
    # token = get_token()
    token = '24.e78c9feb6ded277f644bc9f1da926c40.2592000.1483444662.282335-8779558'
    url = 'http://tsn.baidu.com/text2audio?tex=主人，你好&tok='+token+'&ctp=1&cuid=4545&lan=zh'
    data = urllib.urlopen(url).read()
    filepath = 'tt.mp3'
    f = file(filepath, 'wb')
    f.write(data)
    f.close()

    pygame.mixer.init()
    print("播放音乐1")
    track = pygame.mixer.music.load("tt.mp3")
    pygame.mixer.music.play()
    time.sleep(6)
    # print data
