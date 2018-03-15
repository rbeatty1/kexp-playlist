"""
goal output: csv file containing artist - song name for each of the songs in the latest KEXP Music That Matters
             podcast

title: kexp-get.py
author: robert beatty
date: march 14, 2018
"""

from urllib import request as r
from timeit import default_timer as t
from bs4 import BeautifulSoup
from datetime import datetime as dt
import re

time_start = t()
today = dt.now()
day, month, year = today.day, today.month, today.year
today = "{0}/{1}/{2}".format(month,day,year)
print("start...\n")


# it's a globalized world
kv_latest = []
lines = []

time_siteaccess_start = t()
x = r.urlopen('https://tunein.com/radio/Music-That-Matters-Podcast-p117040/', data=None, timeout=5) # access webpage
time_siteaccess_end = t()
time_siteaccess_duration = round((time_siteaccess_end - time_siteaccess_start),2)
# check server code
if x.getcode() != 200: 
	print("[!] Warning [!]")
else:
	print("successfully accessed website") 
	print("connected to website in {}s\n".format(time_siteaccess_duration))

# see if there's a new podcast today...
try:
	time_tb1_start = t()
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
		print("[!] Warning -- dump failed\n")
	date = kv_latest[1]['v']
	if date == today:
		print('nyet\n')
	else:
		print('yas queen')
	time_tb1_end = t()
	time_tb1_duration = round((time_tb1_end - time_tb1_start),2)
	print("try block one completed in {}s\n".format(time_tb1_duration))
except:
	print("[!] Warning -- in try block 1 [!]")

# TRY BLOCK TWO: let's create a csv(?) containing the songs aired on the latest podcast
try:
	time_tb2_start = t()
	title_seg = re.split(",\s", kv_latest[0]['v'])
	title_seg = re.split("\s-\s", title_seg[1])
	title_vol, title_name = title_seg[0], title_seg[1]
	lines = re.split("\s\d+.\s", kv_latest[3]['v'])
	for i in lines:
		# print(i)
		if re.search("\w+?\s-\s*?\w+?", i):
			print(i)

	time_tb2_end = t()
	time_tb2_duration = round((time_tb2_end - time_tb2_start),2)
	print("try block two completed in {}s\n".format(time_tb2_duration))

except:
	print("[!] Warning -- in try block 2 [!]")


time_end = t()
print("end...")
time_duration = round((time_end - time_start),2)
print("script ran for {}s".format(time_duration))


