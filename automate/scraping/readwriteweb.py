# Automate the boring stuff with Python
# Chapter 11 webscraping - read write web

import requests


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
