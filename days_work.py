P = int(input()) # liters of paint 
B = int(input()) # liters of paint per badge
D = int(input()) # selling price

badges = P // B
badge_sales = badges * D

rem_paint = P % B

income = badge_sales + rem_paint
print(income)



