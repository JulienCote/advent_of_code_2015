row = 2978
column = 3083

x = 1
y = 1

value = 20151125
step = 1

while x <= column or y <= row:
	if x == step and y == 1:
		step += 1
		y = step
		x = 1
	else:
		x += 1
		y -= 1
	value = (value * 252533) % 33554393

	if x == column and y == row:
		print 'The code for the machine is:', value