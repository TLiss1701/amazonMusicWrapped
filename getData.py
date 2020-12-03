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

#exec(open('spotify.py').read())

with open('pkls/cndnsdASL.pkl', 'rb') as f:
    cndnsdASL = pickle.load(f)

bandDict = defaultdict(list)
for song in cndnsdASL:
    bandDict[song[1]].append(song[0])
bandDurDict = defaultdict(list)
for song in cndnsdASL:
    bandDurDict[song[1]].append(song[2])

genreLOL = []
for song in cndnsdASL:
    genreLOL.append(song[3])
allGenres = [genre for genreList in genreLOL for genre in genreList]
genreCount = defaultdict(list)
for genre in allGenres:
    if genre in genreCount:
        genreCount[genre] += 1
    else:
        genreCount[genre] = 1
sortedGenreCount = sorted(genreCount.items(), key=lambda x: x[1], reverse=1)

songInfo = []
for song, band, dur, genres in cndnsdASL:
    dictToAdd = {'Song': song, 'Band': band, 'Duration': dur, 'Genres': genres}
    songInfo.append(dictToAdd)

bandCount = {band: len(songs) for band, songs in bandDict.items()}
bandDurCount = {band: math.trunc(float(sum(dur)/60000)*100)/100 for band, dur in bandDurDict.items()}

sortedBandCount = sorted(bandCount.items(), key=lambda x: x[1], reverse=1)
sortedBandDurCount = sorted(bandDurCount.items(), key=lambda x: x[1], reverse=1)

songList = [i[0] for i in cndnsdASL]
songCount = {song:songList.count(song) for song in songList}
sortedSongCountTups = sorted(songCount.items(), key=lambda x: x[1], reverse=1)
sortedSongCount = [list(x) for x in sortedSongCountTups]
for song in sortedSongCount:
    song.append(list(filter(lambda x: x['Song'] == song[0], songInfo))[0]['Band'])


totalMinListened = sum(n for _, n in sortedGenreCount)
topGenre = sortedGenreCount[0][0]

f = open("data/Band_Time_Listened.csv", "w+")
f.close()
with open("data/Band_Time_Listened.csv", mode='w', newline='', encoding="utf-8") as writefile:
    writer = csv.writer(writefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Band', 'Time Listened (min)'])
    for bands in sortedBandDurCount:
        writer.writerow([bands[0], bands[1]])

f = open("data/Songs_Most_Listened.csv", "w+")
f.close()
with open("data/Songs_Most_Listened.csv", mode='w', newline='', encoding="utf-8") as writefile:
    writer = csv.writer(writefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Song', 'Band', 'Number of Times Listened'])
    for songs in sortedSongCount:
        writer.writerow([songs[0], songs[2], songs[1]])

visualPacket = {
    'Artists': [sortedBandDurCount[0][0],sortedBandDurCount[1][0],sortedBandDurCount[2][0],sortedBandDurCount[3][0],sortedBandDurCount[4][0]],
    'Songs': [sortedSongCount[0][0],sortedSongCount[1][0],sortedSongCount[2][0],sortedSongCount[3][0],sortedSongCount[4][0]],
    'minListened': totalMinListened,
    'topGenre': titlecase(topGenre)
}

f = open("pkls/visualPacket.pkl","wb")
pickle.dump(visualPacket,f)
f.close()