# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:43:19 2017

@author: energ
"""
import subprocess
import os
import hashlib

def printPath():
    try:
        PATH = input('Введите путь >> ')
        print(os.listdir(PATH))
        subprocess.Popen('explorer "%s"'%(PATH))
        return PATH
    except(FileNotFoundError,OSError,UnicodeEncodeError):
        print('Введите путь правильно!')
        printPath() # повтореый вызов функции

PATH = printPath()
filez = os.listdir(PATH)

##############MD5
def getMD5sum(fileName):
    hashs = hashlib.md5()
    
    fd = open(fileName, 'r')
    b = fd.read()
    hashs.update(b.encode('utf-8'))
    fd.close()
    return hashs.hexdigest()


dict = {}
dictDublicates = {}
for top, dirs, files in os.walk(PATH):
    for num in files:
        fname =  os.path.join(top, num)
        fname = str(fname)
        md5sum = getMD5sum(fname)
        print(md5sum, 'utf-8')
        if md5sum  in dict.keys():
            dictDublicates[md5sum] = str(fname + ';  ' + dict[md5sum])
        dict[md5sum] = fname
            
print(dict,'\n')
print('Файлы дубликаты:',dictDublicates)