# reds are eaten one at a time 16 seconds
# everything else eaten 7 at a time (one color finished first) 13 seconds
box = 0
contents = ''
box_time = 0
color_time = 0
line = ''

def color_time(color):
	count = contents.count(color)
	if count % 7 == 0:
		color_time = (count / 7) * 13
	else:
		color_time = (count // 7 + 1) * 13
	box_time += color_time
	color_time = 0
	count = 0 

while  line != 'end of box':
	line = str(input())
	contents = contents.append.input()
color_time("orange")
color_time("blue")
color_time("green")
color_time("yellow")
color_time("pink")
color_time("violet")
color_time("brown")
box_time += red * 16
print(box_time)
box_time = 0
box += 1
contents = ''
								