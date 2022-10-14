adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

questions = int(input())
answers = input()

adrian_correct = 0
bruno_correct = 0
goran_correct = 0
max_count = 0

for i in range(questions):
    if adrian[i % 3] == answers[i]:
        adrian_correct += 1
    if bruno[i % 4] == answers[i]:
        bruno_correct += 1
    if goran[i % 6] == answers[i]:
        goran_correct += 1
        
if adrian_correct > bruno_correct:
        max_count = adrian_correct
else: max_count = bruno_correct

if max_count < goran_correct:
        max_count = goran_correct        
print(max_count)

if adrian_correct == max_count:
    print('Adrian')
if bruno_correct == max_count:
    print('Bruno')
if goran_correct == max_count:
    print('Goran')