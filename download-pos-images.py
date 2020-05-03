#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 11:42:56 2018

@author: KaranJaisingh
"""

import cv2
from six.moves import urllib
import numpy as np
import os

def store_raw_images():
    neg_image_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    filename = "urls_pos.txt"
    with open(filename) as f:
        neg_image_urls = f.read()

    if not os.path.exists('pos'):
        os.makedirs('pos')

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(pic_num, i)
            urllib.request.urlretrieve(i, 'pos/'+str(pic_num)+'.jpg')
            img = cv2.imread('pos/'+str(pic_num)+'.jpg')
            resized_image = cv2.resize(img, (300, 300))
            cv2.imwrite('pos/'+str(pic_num)+'.jpg', resized_image)
            pic_num += 1
            if(pic_num > 1000):
                return

        except Exception as e:
            print(str(e))

store_raw_images()