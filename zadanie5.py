# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:12:59 2017
@author: energ
"""
import re

def SplitLine(TextV):
    Text = ''
    splitText = TextV.split(' ')
    for i in range(len(splitText)):
        pattern = re.compile('[A-Z]{1}[a-z]+\d{4}|[A-Z]{1}[a-z]+\d{2}')
        Text = pattern.findall(splitText[i])
        #print(Text)
        if Text != None:
            print(Text)
        
Line = input('Введите строку >> ')
SplitLine(Line)