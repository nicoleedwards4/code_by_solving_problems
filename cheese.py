width = int(input())
cheese = int(input())
rating = ''


if width == 3 and cheese >= 95:
	rating = 'absolutely'
elif width ==1 and cheese <= 50:
	rating = 'fairly'
else:
	rating = 'very'

out = f"C.C. is {rating} satisfied with her pizza."

print(out)