"""
Let's see if we can pin down the XML to read the newest MTM podcast information

title: get_kexpurl.py
author: robert beatty
date: march 14, 2018
"""

from urllib import request as r
from timeit import default_timer as t
from bs4 import BeautifulSoup
from datetime import datetime as dt

time_start = t()
today = dt.now()
day, month, year = today.day, today.month, today.year
today = "{0}/{1}/{2}".format(month,day,year)

x = r.urlopen('https://tunein.com/radio/Music-That-Matters-Podcast-p117040/', data=None, timeout=5) # access webpage

# check server code
if x.getcode() != 200: 
	print("[!] Warning [!]")
else:
	print("successfully accessed website")

# see if there's a new podcast today...
try:
	kv_latest = []
	dump = BeautifulSoup(x, 'lxml')
	if len(dump) >0: 
		a = dump.find(id="container-0") 
		b = a.contents[1].strings
		cnt = 0
		for str in b:
			kvp ={'i':cnt,
				'v':str
				}
			kv_latest.append(kvp)
			cnt += 1
	else:
		print("[!] Warning -- dump failed")
	date = kv_latest[1]['v']
	print(date)
	if date != today:
		print('nyet')
	else:
		print('yas queen')
except:
	print("[!] Warning -- in try block 1 [!]")



time_end = t()
time_duration = round((time_end - time_start),2)
print("script ran for {}s".format(time_duration))


