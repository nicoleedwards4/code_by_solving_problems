n = int(input())

t = 0
s = 0

for i in range(n):
	text = str(input()).lower()
	t += text.count('t')
	s += text.count('s')

if t > s:
	print('English')
else: 
	print('French')