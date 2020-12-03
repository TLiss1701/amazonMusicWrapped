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
from titlecase import titlecase
from PIL import Image, ImageDraw, ImageFont
import pickle

with open('pkls/visualPacket.pkl', 'rb') as f:
    visualPacket = pickle.load(f)

img = Image.new('RGB', (1920, 1080), color = (20, 110, 180))


titleFont = ImageFont.truetype('fonts\GothamBold.ttf', 35)
font = ImageFont.truetype('fonts\GothamMedium.ttf', 35)
bigFont = ImageFont.truetype('fonts\GothamBold.ttf', 70)
genreFont = ImageFont.truetype('fonts\GothamBold.ttf', 50)
topFont = ImageFont.truetype('fonts\GothamBold.ttf', 90)

d = ImageDraw.Draw(img)

d.text((400, 100), "Amazon Music Wrapped", fill=(0, 168, 225), font=topFont)

d.text((920, 250), "TOP ARTISTS", fill='white', font=titleFont)
d.text((920, 310), "1", fill='white', font=titleFont)
d.text((920, 370), "2", fill='white', font=titleFont)
d.text((920, 430), "3", fill='white', font=titleFont)
d.text((920, 490), "4", fill='white', font=titleFont)
d.text((920, 550), "5", fill='white', font=titleFont)
d.text((950, 310), visualPacket['Artists'][0], fill='yellow', font=font)
d.text((950, 370), visualPacket['Artists'][1], fill='yellow', font=font)
d.text((950, 430), visualPacket['Artists'][2], fill='yellow', font=font)
d.text((950, 490), visualPacket['Artists'][3], fill='yellow', font=font)
d.text((950, 550), visualPacket['Artists'][4], fill='yellow', font=font)

d.text((1420, 250), "TOP SONGS", fill='white', font=titleFont)
d.text((1420, 310), "1", fill='white', font=titleFont)
d.text((1420, 370), "2", fill='white', font=titleFont)
d.text((1420, 430), "3", fill='white', font=titleFont)
d.text((1420, 490), "4", fill='white', font=titleFont)
d.text((1420, 550), "5", fill='white', font=titleFont)
d.text((1450, 310), visualPacket['Songs'][0], fill='yellow', font=font)
d.text((1450, 370), visualPacket['Songs'][1], fill='yellow', font=font)
d.text((1450, 430), visualPacket['Songs'][2], fill='yellow', font=font)
d.text((1450, 490), visualPacket['Songs'][3], fill='yellow', font=font)
d.text((1450, 550), visualPacket['Songs'][4], fill='yellow', font=font)

d.text((920, 700), "MINUTES LISTENED", fill='white', font=titleFont)
d.text((920, 760), str(visualPacket['minListened']), fill='yellow', font=bigFont)

d.text((1420, 700), "TOP GENRE", fill='white', font=titleFont)
d.text((1420, 760), visualPacket['topGenre'], fill='yellow', font=genreFont)

bandCover = Image.open('imgs/Genesis.jpg')

img.paste(bandCover, (100, 220))

img.save('amazonWrapped.png')