cases= [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]
eliminated = 0

cases_opened = int(input())

for i in range(cases_opened):
	caseno = int(input())
	eliminated += cases[caseno-1]

offer = int(input())

if offer > (sum(cases)-eliminated)/(len(cases)-cases_opened):
	print('deal')
else:
	print('no deal')
