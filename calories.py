# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:30:44 2022

@author: nedwards1
"""
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

burger_dict = { 1:461, 2:431, 3:420, 4:0 }
side_dict = { 1:100, 2:57, 3:70, 4:0 }
drink_dict = { 1:130, 2:160, 3:118, 4:0 }
dessert_dict = { 1:167, 2:266, 3:75, 4:0 }

burger_cals = burger_dict[burger]
side_cals = side_dict[side]
drink_cals = drink_dict[drink]
dessert_cals = dessert_dict[dessert]

total_cals = burger_cals + side_cals + drink_cals + dessert_cals

out = f"Your total Calorie count is {total_cals}."

print(out)

