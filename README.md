# **KEXP-Playlist**
**Author:** Robert Beatty

_**Disclaimer**: this project isn't affiliated with DVRPC except for the fact that I want to listen to my KEXP playlist at work_


This is a fun little side project I've been thinking about for a while
to help brush up on some python skills.

The Seattle Radio Station comes out with a weekly podcast called "Music That Matters"
and I love to listen to it. But you see, I also really love spotify, so why not combine the two
and get my favorite music podcast right into what I'm already using to pump tunes anyway?

The goal here is to get a script that can run every Friday and scrape the podcast lists to see
if theres a new podcast available and then add those podcasts to an existing playlist.

## **Getting Started**
**Dependencies** 

* BeautifulSoup4
* Spotipy
* lxml
  
**Installation**

`git clone https://github.com/rbeatty1/kexp-playlist.git`

`cd env/Scripts`

`activate`

`cd ../..`

`python kexp-get.py`

