"""
goal output: grab latest KEXP Music that Matters playlist, search spotify for the songs, and add any song that returns a match
title: kexp-get.py
author: robert beatty
date: July 2, 2018
"""

from urllib import request as r
from timeit import default_timer as t
from bs4 import BeautifulSoup
import re, os, spotipy, urllib
import spotipy.util as util

# it's a globalized world
kv_latest = []
lines = []

x = r.urlopen('http://feeds.kexp.org/kexp/musicthatmatters', data=None, timeout=5) # jawn
# good jawn?
if x.getcode() != 200:
	print("[!] Warning [!]")
else:
	print("successfully accessed website")


# new jawn?
try:
	t_tb1_s = t()
	dump = BeautifulSoup(x, 'lxml-xml')
	if len(dump) >0:
		a = dump.find_all("description")
		new = str(a[1].get_text())
	else:
		print("dump failed")
except Exception as e:
	print(e.message)

# TRY BLOCK TWO: let's create a csv(?) containing the songs aired on the latest podcast
try:
	lines = re.split("\s\d+.\s", new)
	cnt = 1
	song_list = []
	# make a jawn
	# open jawn
	for i in lines:
		# that good jawn
		m = re.match(r'^(.*?)\s-\s(.*?)$', i)
		if '<' in i:
			j = str(i)
			spt = j.split('<')
			spt2 = spt[0].split(' - ')
			song = {
				'track': cnt,
				'artist': spt2[0],
				'name': spt2[1]
			}
			song_list.append(song)
			del song
			cnt +=1
		elif m:
			spt = i.split(' - ')
			# print(spt[1])
			song = {
				'track': cnt,
				'artist': spt[0],
				'name': spt[1]
			}
			song_list.append(song)
			del song
			cnt +=1
except Exception as e:
	print(e.message)


## TRY BLOCK 3: Spotify stuff
scope = 'playlist-modify-private'
client_id='a1cf45685b554834a0af87822b902476'
client_secret= str(input('> Insert Client Secret code: '))
redirect_uri='https://www.google.com/'
try:
	username = str(1246074730) ## get from spotify app. ID : 1246074730
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except:
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)
playlist_id = '06YBjhkywYl6HEy7FMZaA9'
success = []
failed = []
cnt = 1
for song in song_list:
	q = "track:{} artist:{}".format(song['name'],song['artist'])
	encoded = urllib.parse.quote(q)
	result = sp.search(q=q,limit=1,offset=0,type='track')
	if len(result['tracks']['items']) != 0:
		results_list = result['tracks']['items'][0]
		if results_list['album']['artists'][0]['name'] != song['artist'] and results_list['name'] != song['name']:
			failed.append(song['name'])
		else:
			success.append(results_list['uri'])
	else:
		failed.append(song['name'])
#
	cnt +=1
	del result
sp.user_playlist_add_tracks(username, playlist_id, success)
print("{} songs out of {} added for a {}% success rate for this week".format(len(success), (len(success)+len(failed)), round(((len(success)/(len(success)+len(failed)))*100),2)))
print("end...")


