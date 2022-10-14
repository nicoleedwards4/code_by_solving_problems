pw = input()

#three lowercase
#two uppercase
#one digit

lower = 0
upper = 0
digit = 0

for i in range(len(pw)):
	if pw[i].islower():
		lower += 1
	elif pw[i].isupper():
		upper += 1
	elif pw[i].isnumeric():
		digit += 1

check = ''
if 8 <= len(pw) <= 12 and lower >=3 and upper >= 2 and digit >= 1:
	check = 'Valid' 
else:
	check = 'Invalid'

print(check)