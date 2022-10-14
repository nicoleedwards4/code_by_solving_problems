N = int(input()) #next number in the take a number machine

next_number = N
late_today = 0 
now_waiting = 0 

action = input()
while action != 'EOF':
	if action == 'TAKE':
		late_today += 1			
		now_waiting += 1
		next_number += 1 
		if next_number == 1000:
			next_number = 1
	if action == 'SERVE' and now_waiting > 0:
		now_waiting -= 1
	if action == 'CLOSE':
		print(f"{late_today} {now_waiting} {next_number}")
		late_today = 0 
		now_waiting = 0
	action = input()
