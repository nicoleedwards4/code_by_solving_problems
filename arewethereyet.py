# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:08:10 2022

@author: nedwards1
"""
def distance_between(lst, i, j):
    if i < j:
        city1 = i
        city2 = j
    else: 
        city1 = j
        city2 = i
    total = 0
    for k in range(city1, city2):
        total += lst[k]
    return total 

lst = input.split()

# converts inputs to int 
for i in range (len(lst)):
    list[i] = int(lst[i])

for i in range(len(lst) +1):
    distances = []
    for j in range(len(lst+1)):
        distances.append(str(distance_between(lst, i, j)))
    print(''.join(distances))
    