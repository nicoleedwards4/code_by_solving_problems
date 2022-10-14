N = input()

honi = 'HONI'
next = 0
HONI_blocks = 0 

for i in range(len(N)):
	if N[i] == honi[next]:
		if next < 3:
			next += 1
		else:
			next = 0
			HONI_blocks += 1
	
print(HONI_blocks)
