# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:41:12 2017

@author: energ
"""

import re



#######
def searching(text):
    #text = text.lower
    for i in range(len(text)):
        pattern = re.compile(r'192.\d{0,3}.\d{0,3}.\d{0,3}')
        result = pattern.findall(text[i])
        searchForResult = pattern.search(text[i])
        if searchForResult != None:
            print('Строка ',i,' Позиция ',searchForResult.span(),' : ',result)
            

#######
def workWithFile(pathToFile):
    rfile = open(pathToFile)
    #fileString = rfile.read()
    fileString = rfile.readlines()   
    searching(fileString)
    

#######
finish_it = False
while finish_it !=True:
    try:
        _pathToFile = input('Введите путь к файлу (I:\Python\Лаба 2\zad4\file.txt)>> \n')
        workWithFile(_pathToFile)
        finish_it = True    
    except(FileNotFoundError,OSError):
        print('Файл не найден!')