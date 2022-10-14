# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:47:58 2022

@author: nedwards1
"""
import os
os.chdir("C:/Users/nedwards1/OneDrive - City of Tacoma/Python Scripts")

def read_cows(input_file, num_cows):
    favorites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites

def cows_with_favorites(favorites, pasture):
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows

def types_used(favorites, cows, pasture_types):
    used = []
    for cow in cows:
            pasture_a = favorites[cow][0]
            pasture_b = favorites[cow][1]
            if pasture_a <len(pasture_types):
                    used.append(pasture_types[pasture_a])
            if pasture_b < len(pasture_types):
                    used.append(pasture_types[pasture_b])
            return used

def smallest_available(used):
    grass_type = 1
    while grass_type is used:
        grass_type = grass_type +1
    return grass_type

def write_pastures(output_file, pasture_types):
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')
# Main Program
input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

# Read input
lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file, num_cows)

pasture_types = [0]

for i in range(1, num_pastures + 1):
    # Identify cows that care about pasture
    cows = cows_with_favorites(favorites, i) 
    
    # Eliminate grass types for pasture
    eliminated = types_used(favorites, cows, pasture_types)

    # Choose smallest-numbered grass type for pasture
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)
    
# Write output
pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()