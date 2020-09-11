#! /usr/bin/env python

# Project 10 Unneeded Files

import os
from pathlib import Path
import pprint

largeSize = 1000 * 100
fileSizeDic = {}

def unNeeded(folder):
    folder = os.path.abspath(folder)    # Make sure folder is absolute
    
    for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            filePath = Path(foldername)/Path(file)
            fileSize = os.path.getsize(filePath)
            if fileSize > largeSize:
                fileSizeDic[filePath] = fileSize 
    fileSizeSort = sorted(fileSizeDic.items(), key=lambda x: x[1], reverse=True)
    
    for  i in fileSizeSort:
        print(str(i[0]) + ':' + str(i[1] / 1000) + 'KB')
    # pprint.pprint(fileSizeSort)

unNeeded('/home/takatani/python/practice/automate')

