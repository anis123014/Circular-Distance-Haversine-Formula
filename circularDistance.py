# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:49:40 2017

@author: Anisur Rahman Anis
"""
import pandas as pd
import numpy as np
import csv
import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees).
    Source: https://gis.stackexchange.com/a/56589/15183
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c *1000
    return km

reader1= np.array(pd.read_csv('1.csv'))
reader2= np.array(pd.read_csv('2.csv'))
print("Id1 \tId2 \tDistance (m)\t Duration (s)")
for id1, row1 in enumerate(reader1):
    for id2, row2 in enumerate(reader2):
        floats1 = list(map(float, row1[1:]))
        floats2 = list(map(float, row2[1:]))
       # print(floats1)
        #print(floats2)
        print(id1,id2,int(np.round(haversine(floats1[1],floats1[0],floats2[1],floats2[0]))),int((int(np.round(haversine(floats1[1],floats1[0],floats2[1],floats2[0]))))*.18))
        #print (int(np.round(haversine(floats1[1],floats1[0],floats2[1],floats2[0]))))*.18