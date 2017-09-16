#!bin/python 
#-*- coding:utf-8 -*-
from olp import Nan 
import urllib2
import urllib
from bs4 import BeautifulSoup
import os,re
from PIL import Image, ImageDraw, ImageFont
import sys
reload(sys)

re=Nan()
sys.setdefaultencoding("utf-8")
im= Image.new('RGB',(460,len(re)*40),0xffffff)
draw=ImageDraw.Draw(im)
width,height=im.size
font = ImageFont.truetype("./font/MSYHBD.TTC",14)
fontcolor = (14,77,157)
f=['cout',"bi",'c++','java']
for i,h in  enumerate(re):
	j=8+20*i
	draw.rectangle(((10,j),(re[i],j+10)),fill=(223,223,223));
	draw.text((re[i],j),f[i], fill=fontcolor,font=font)
im.save('k.png')
im.close()

