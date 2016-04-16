#coding=utf8
# TODO
import md5, base64, random
import requests, json
import os, sys


headers = {
    'Cookie': 'appver=2.0.2',
    'Referer': 'http://music.163.com',
}

def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result

def search(name, limit = 10):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 100,
            'offset': 0,
            'sub': 'false',
            'limit': limit,
    }
    r = requests.post(search_url, params, headers = headers)
    artists = r.json()
    if artists['code'] == 200 and artists['result']['artistCount'] > 0:
        return artists['result']['artists']
    else:
        return None

def search_album_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 10,
            'offset': 0,
            'sub': 'false',
            'limit': 20
    }
    r = requests.post(search_url, params, headers = headers)
    resp_js = r.json()
    if resp_js['code'] == 200 and resp_js['result']['albumCount'] > 0:
        return resp_js['result']
        # return result['albums'][album_id]
    else:
        return None

def search_song_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 1,
            'offset': 0,
            'sub': 'false',
            'limit': 20
    }
    r = requests.post(search_url, params, headers = headers)
    resp_js = r.json()
    if resp_js['code'] == 200 and resp_js['result']['songCount'] > 0:
        return resp_js['result']
        # song_id = result['songs'][select_i-1]['id']
        # TODO
        detail_url = 'http://music.163.com/api/song/detail?ids=[%d]' % song_id
        r = requests.get(detail_url)
        song_js = r.json()
        return song_js['songs'][0]
    else:
        return None

def get_artist_albums(artist):
    albums = []
    offset = 0
    while True:
        url = 'http://music.163.com/api/artist/albums/%d?offset=%d&limit=50' % (artist['id'], offset)
        r = requests.get(url, headers = headers)
        tmp_albums = r.json()
        albums.extend(tmp_albums['hotAlbums'])
        if tmp_albums['more'] == True:
            offset += 50
        else:
            break
    return albums

def get_album_songs(albumId):
    url = 'http://music.163.com/api/album/%d/' % albumId
    r = requests.get(url, headers = headers)
    songs = r.json()
    return songs['album']['songs']

def save_song_to_disk(song, folder):
    name = song['name']
    fpath = os.path.join(folder, name+'.mp3')
    if not os.path.exists(folder): os.mkdir(folder)
    if os.path.exists(fpath): return

    song_dfsId = str(song['bMusic']['dfsId'])
    url = 'http://m%d.music.126.net/%s/%s.mp3' % (random.randrange(1, 3), encrypted_id(song_dfsId), song_dfsId)
    r = requests.get(url, headers = headers)
    with open(fpath, 'wb') as f:
        f.write(r.content)

def download_song_by_search(name, folder='.'):
    song = search_song_by_name(name)
    if not song:
        print('Not found ' + name)
        return

    if not os.path.exists(folder):
        os.makedirs(folder)
    save_song_to_disk(song, folder)


def download_album_by_search(name, folder='.'):
    album = search_album_by_name(name)
    if not album:
        print('Not found ' + name)
        return
    
    name = album['name']
    folder = os.path.join(folder, name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    songs = get_album_songs(album)
    for song in songs:
        save_song_to_disk(song, folder)

if __name__ == '__main__':
    pass