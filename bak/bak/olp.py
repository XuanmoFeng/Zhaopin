#!bin/python 
#-*- coding:utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup
import os,re
def Nan():
	i =urllib.urlopen("http://job.xidian.edu.cn/html/zpxx/nxqzph/")
	soup=BeautifulSoup(i)
	tabel =soup.findAll('table')
	tab=tabel[0]
	mo=tab.findAll('tr')
	print len(mo)
	for tr in mo:
		for td in tr.findAll('td'):
			print td.getText()
Nan()
