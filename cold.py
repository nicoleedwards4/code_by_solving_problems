nlines = int(input())

for datasest in range(nlines):
	result = ''
	line = input()
	i = 0
	
	while i< len(line):
		total = 1
		while i < len(line) - 1 and line[i] == line[i+1]:
			i += 1
			total += 1
		result = result + f{total} {line[i]} '
		i += 1
	print(result.strip())
			
			