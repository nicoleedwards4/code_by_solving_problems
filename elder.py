curr_wiz = input()
duels = int(input())

diff_wizards = 0

for i in range(duels):
	duel_str = input()
	if duel_str[2] == curr_wiz:
		curr_wiz = duel_str[0]
		diff_wizards += 1

  
print(curr_wiz)
print(duels)