#!bin/python 
#-*- coding:utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup
import os,re
def Bei(url):
	i =urllib.urlopen(url)
	soup=BeautifulSoup(i)
	tabel =soup.findAll('table')
	tab=tabel[0]
	my=''
	for tr in tab.findAll('tr'):
		mtr='<tr>'
		for td in tr.findAll('td'):
			mi='<td>'
			hre=td.findAll('a')
			if hre:
				mi+='<a href="http://job.xidian.edu.cn'+hre[0].get('href')+'">'+td.getText()+'</a><td>'
			elif td:
				mi+=td.getText()+'</td>'
			else:
				pass
			mtr+= mi
		mtr+='</tr>'
		my+=mtr
	return my	
