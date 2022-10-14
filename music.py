a_minor = 'ADE'
c_major = 'CFG'

line = input()

accented = ''
accented = line[0]
for i in range(1, len(line)):
	if line[i] == "|":
		accented += line[i+1]

a_tones = accented.count('A') + accented.count('D') + accented.count('E')
c_tones = accented.count('C') + accented.count('F') + accented.count('G')


print('accented')
print('a_tones')
print('c_tones')

print('C-dur' if c_tones > a_tones else 'A-mol')