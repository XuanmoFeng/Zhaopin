#!bin/python 
#-*- coding:utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup
import os,re,sys
reload(sys)
sys.setdefaultencoding("utf-8")
def Nan():
	re=[]
	XianBi=0
	CPP=0
	JAVA=0
	
	i =urllib.urlopen("http://job.xidian.edu.cn/html/zpxx/bxqzph/")
	soup=BeautifulSoup(i)
	tabel =soup.findAll('table')
	tab=tabel[0]
	mo=tab.findAll('tr')
	re.append(len(mo))
	print "西安电子科技大学北校区有笔试的宣讲会\n"
	for tr in mo:
		hh=" "
		for td in tr.findAll('td'):
			m=td.findAll('a')
			hh+=td.getText()+"\t"
			if m:
				h=urllib.urlopen('http://job.xidian.edu.cn'+m[0].get('href'))
				w= h.read()
				if ("现场"in w) and("笔试" in w)and("在线笔试" not in w):
					XianBi+=1
				if ("C++" in w)or ("c++" in w):
					CPP+=1
				if ("Java" in w)or("java" in w)or("JAVA" in w):
					JAVA+=1
	re.append(CPP)
	re.append(JAVA)
	re.append(XianBi)
	return re
