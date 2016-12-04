#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

import compareImgs


class detectBody:
    snapshot_url = 'http://pi1.myraspberry.pipa123.cn/?action=snapshot'
    stream_url = 'http://pi1.myraspberry.pipa123.cn/?action=stream'
    def get_first_img(self):
        return 'test.jpg'

    @classmethod
    def get_newest_img(self,filepath='resources/imgs/newest.jpg'):
        data = urllib.urlopen(self.snapshot_url).read()
        f = file(filepath,'wb')
        f.write(data)
        f.close()
        return filepath

    @classmethod
    def compare_imgs(self):
        return compareImgs.calc_similar_by_path('../resources/imgs/test1.jpg','../resources/imgs/newest.jpg')
