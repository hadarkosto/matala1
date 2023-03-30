# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:03:25 2023

@author: kosto
"""

def revword(word:str): 
    word=word[::-1].lower()
    return word

def countword()->int: 
    text = open('text.txt', 'r')
    lines = text.readlines()
    line1 = True
    counter = 1
    for i in lines:
        if line1:
            word = i.lower().replace('\n','')
            line1 = False
            continue
        line = i.split()
        for j in line:
            if word == revword(j):
                counter=counter+ 1
    return counter

print(countword())