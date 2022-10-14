# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:54:40 2022

@author: nedwards1
"""

year = int(input())
year += 1

while not len(set(str(year))) == len(str(year)):
    year += 1

print(year)