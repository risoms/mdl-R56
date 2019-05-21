# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:53:01 2016

@author: sr38553
"""

from PIL import Image, ImageOps, ImageDraw, ImageEnhance
import glob
import os

try: #use _file_ in most cases
    dir = os.path.dirname(__file__)
except NameError:  #except when running python from py2exe script
    import sys
    dir = os.path.dirname(sys.argv[0])


data = os.path.abspath("practice_instructions/")
img_num = 0
#loop through all found images
for i, f in enumerate(os.listdir(data)):
    src = os.path.join(data, f)
    dst = os.path.join(data, 'pi-'+str(img_num)+'.png')
    os.rename(src, dst)
    img_num = img_num+1