# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:12:29 2022

@author: nedwards1
"""

presses = int(input())

a_count = 0
b_count = 1

for i in range(presses -1):
        new_a_count = b_count
        new_b_count = a_count + b_count
        a_count = new_a_count
        b_count = new_b_count
        
print(f"{a_count} {b_count}")
      
      