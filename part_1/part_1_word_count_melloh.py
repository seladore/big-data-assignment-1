# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:03:21 2017

@author: abeme
"""

file=open("C:\\Users\\abeme\\Desktop\\BigData\\FilestobefedintoPython\\CompleteWorkofShakespeare.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v