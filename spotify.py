from selenium import webdriver
import time
from collections import defaultdict
import pprint
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging
import math
import csv
import pickle
from titlecase import titlecase

exec(open('scraper.py').read())

with open('pkls/allSongList.pkl', 'rb') as f:
    allSongList = pickle.load(f)

client_id = "6f51739589894b089686876c420ec812"
client_secret = "fce52ef8f7a44305893701b1c01cd549"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

with open('yourlog.log', 'w'):
    pass

logging.basicConfig(filename='scraper.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

cndnsdASL = []
for song in allSongList:
    if song[0] != None:
        cndnsdASL.append(song)

for song in cndnsdASL:
    song[0] = re.sub("[\(\[].*?[\)\]]", "", song[0]).strip()
    song[1] = re.sub("[\(\[].*?[\)\]]", "", song[1]).strip()

i = 1
for song in cndnsdASL:
    query = "artist:" + song[1] + " track:" + song[0]
    qRes = sp.search(q=query, type="track", limit=1)
    try:
        song.append(qRes['tracks']['items'][0]['duration_ms'])
        print("[" + str(i) + "/" + str(len(cndnsdASL)) + "] Duration found for song " + qRes['tracks']['items'][0]['name'])
    except:
        song.append(0)
        logging.error("Spotify API Duration Fetch Error for Song " + song[0])
    try:
        song.append(sp.artist(qRes['tracks']['items'][0]['album']['artists'][0]['id'])['genres'])
        print("[" + str(i) + "/" + str(len(cndnsdASL)) + "] Genre found for song " + qRes['tracks']['items'][0]['name'])
    except:
        song.append([])
        logging.error("Spotify API Genre Fetch Error for Song " + song[0])
    i += 1

f = open("pkls/cndnsdASL.pkl","wb")
pickle.dump(cndnsdASL,f)
f.close()