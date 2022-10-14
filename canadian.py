vowels = 'aeiouy'

word = str(input())
correct_spelling = ''

while word != 'quit!':
	if len(word) > 4 and word[-3] not in vowels and word[-2:] == 'or':
		correct_spelling = word[:-2]+'our'
	else: 
		correct_spelling = word
	print(correct_spelling)
	word = str(input())


