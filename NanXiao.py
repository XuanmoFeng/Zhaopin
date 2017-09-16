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
def Him(url, filename):
	i=urllib.urlopen(url)#
	soup=BeautifulSoup(i)
	tabel=soup.findAll('table')
	tab=tabel[0]
	mo=tab.findAll('tr')
	num =len(mo)
	im= Image.new('RGB',(600,num*30),0xffffff)
	draw=ImageDraw.Draw(im)
	width,height=im.size
#	for i in range(1,num):
#		y=i*30+10
#		draw.line(((10, y),(width-10,y)) , fill=(225,225,225))
#	draw.line(((10, 1),(10,height-20)) , fill=(225,225,225))
#	draw.line(((width-10, 1),(width-10,height-20)) , fill=(225,225,225))
	draw.rectangle(((10,1),(width-10,40)),fill=(223,223,223));
	font = ImageFont.truetype("/root/9-9/font/MSYHBD.TTC",14)
	fontcolor = (14,77,157)
	draw.text((20,10), u"时间", fill=fontcolor,font=font)
	draw.text((140,10), u"地点", fill=fontcolor,font=font)
	draw.text((280,10), u"公司", fill=fontcolor,font=font)
	i=1;
	for tr in mo:
		y=i*30+10
		i+=1
		m=1
		for td in tr.findAll('td'):
			if m==1:
				draw.text((20,y),td.getText(), fill=(175,215,237),font=font)
			elif m==2:
	
				draw.text((140,y),td.getText(), fill=(92,167,186),font=font)
			elif m==3:
				draw.text((280,y),td.getText(), fill=(255,66,93),font=font)
			else:
				pass
			m+=1
		im.save(filename)
