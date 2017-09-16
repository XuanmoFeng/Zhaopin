#!bin/python 
#-*- coding:utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup
import os,re
from PIL import Image, ImageDraw, ImageFont
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def mergej(files, output_file):
    tot = len(files)
    img = Image.open(files)
    w, h = img.size[0], img.size[1]
    merge_img = Image.new('RGB', (w, h * tot), 0xffffff)
    j = 0
    for f in files:
        img = Image.open(f)
        merge_img.paste(img, (0, j))
        j += h
    merge_img.save(output_file)

i=urllib.urlopen("http://job.xidian.edu.cn/html/zpxx/nxqzph/")
soup=BeautifulSoup(i)
tabel=soup.findAll('table')
tab=tabel[0]
mo=tab.findAll('tr')
num =len(mo)

im= Image.new('RGB',(460,num*30),0xffffff)
draw=ImageDraw.Draw(im)
width,height=im.size
for i in range(1,num):
	y=i*30+10
	draw.line(((10, y),(width-10,y)) , fill=(225,225,225))
draw.line(((10, 1),(10,height-20)) , fill=(225,225,225))
draw.line(((width-10, 1),(width-10,height-20)) , fill=(225,225,225))
draw.rectangle(((10,1),(width-10,40)),fill=(223,223,223));
font = ImageFont.truetype("./MSYHBD.TTC",14)
fontcolor = (14,77,157)
draw.text((20,10), u"时间", fill=fontcolor,font=font)
draw.text((140,10), u"地点", fill=fontcolor,font=font)
draw.text((280,10), u"公司", fill=fontcolor,font=font)
for i in range(1,num):
	y=i*30+10
	draw.text((20,y),u"das", fill=fontcolor,font=font)
	draw.text((140,y),u"sdxx", fill=fontcolor,font=font)
	draw.text((280,y), u"dasdasdav ", fill=fontcolor,font=font)
im.save('k.png')
im.close()

