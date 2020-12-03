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
import getpass
from titlecase import titlecase

def scroll(driver, timeout, allSongList):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    i = 0
    while i < 2500:

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        allSongs = driver.find_element_by_xpath('//*[@id="Web.TemplatesInterface.v1_0.Touch.GalleryTemplateInterface.GalleryTemplate_1"]/music-container/div[2]/div/div')
        templist = allSongs.find_elements_by_xpath(".//*")
        for song in templist:
            songtoAdd = []
            songtoAdd.append(song.get_attribute("primary-text"))
            songtoAdd.append(song.get_attribute("secondary-text"))
            allSongList.append(songtoAdd)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
        i =  i + 1
    return allSongList

driver = webdriver.Chrome()

driver.get("https://music.amazon.com/forceSignIn?useHorizonte=true")

print("Username: ", end='')
un = input()
username = driver.find_element_by_name("email")
username.send_keys(un)
password = driver.find_element_by_name("password")
pw = getpass.getpass(prompt='Password: ', stream=None)
password.send_keys(pw)
driver.find_element_by_id("signInSubmit").click()
time.sleep(5)
driver.get("https://music.amazon.com/recently/played/songs")
allSongList = []
allSongList = scroll(driver, 3, allSongList)

f = open("pkls/allSongList.pkl","wb")
pickle.dump(allSongList,f)
f.close()