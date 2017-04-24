# -*- coding: utf-8 -*-
# -*- coding: cp1251 -*-
"""
Created on Sat Apr  8 15:25:27 2017

@author: energ
"""

my_file = open('text.txt','r')       #Только открытие файла

#print(my_file.read())               #Вывод всех символов
my_string = my_file.read()
my_string = my_string.lower()        #Нижний регистр
noSymb = []                          #массив для букв без символов(#!^&*$...)
for i in range(len(my_string)):
    if my_string[i].isalpha():
        noSymb.append( my_string[i] )

dict = {}                            #Частота повторения букв
for i in range(len(noSymb)):
    counter = 0
    for j in noSymb:
        if noSymb[i] == j:
            counter = counter + 1
            dict[noSymb[i]] = counter
                #Сортировка по частоте     
l = lambda x: x[1]
SortedValues = sorted(dict.items(), key=l, reverse=True) 
#-----------------------------------
                                    #Output
print ('Unsorted: \n',dict,"\n\n",'Sorted: \n',SortedValues)
my_file.close()