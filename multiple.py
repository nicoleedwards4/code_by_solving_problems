n = int(input())
string = ''

for i in range(n*2):
	string += input()

correct = 0
for i in range(n):
	if string[i] == string[i+n]:
		correct += 1

print(correct)
	