P = int(input())
N = int(input())
R = int(input())

sick = N
days = 0 
ttl_people = N 

while ttl_people <= P:
	sick = sick * R	
	ttl_people += sick
	days += 1

print(days)