cbv = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

cards_drawn = int(input())
hand = 0
for i in range(cards_drawn):
	value = int(input())
	hand += value
	cbv[value] -= 1

x = 21 - hand

over_x= sum(cbv[x+1:])
under_x= sum(cbv[:x+1])

if over_x >= under_x:
	print('DOSTA')
else:
	print('VUCI')
	
