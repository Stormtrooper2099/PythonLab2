# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:10:17 2017

@author: energ
"""

import os
import re

path = "I:\Python\Лаба 2\zad3\Mus"
#print(path)
basepath = os.path.abspath(os.path.dirname('Mus'))
path = os.path.join(basepath, 'Mus')
#----------------------------------------------

songList = open('I:\Python\Лаба 2\zad3\Mus\SongList.txt','r')
formatedList = songList.readlines()
dict = {}
    
for line in range(len(formatedList)):
    temp = formatedList[line]
    temp2 = formatedList[line]
    temp2 = str(temp2)
    temp2 = re.sub('\n',' ', temp2)
    print('temp2  ' + temp2)
    temp = temp.split(' ')
    dict[temp[1]+'.mp3'] = str(temp2)

for top, dirs, files in os.walk(path):
    for nm in files:
        fname =  os.path.join(top, nm)   
        fname = str(fname)#.encode('utf-8') 
        print(' nm ' + nm)
        print('DICT.KEYS  ',dict.keys())
        if nm in dict.keys():
            os.rename(fname,top+"\\"+dict[nm]+'.mp3')