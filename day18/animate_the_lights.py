import copy

def switching_rule(light, number_neighbor):
	if light == True:
		if number_neighbor not in [2,3]:
			return False
		else:
			return True
	else:
		if number_neighbor == 3:
			return True
		else:
			return False

def number_lit_neighbor(lights, x, y, x_size, y_size):
	number_lights_on_around = 0

	if x > 0 and y > 0 and lights[x-1, y-1]:
		number_lights_on_around += 1
	if y > 0 and lights[x, y-1]:
		number_lights_on_around += 1
	if x < x_size-1 and y > 0 and lights[x+1, y-1]:
		number_lights_on_around += 1
	if x > 0 and lights[x-1, y]:
		number_lights_on_around += 1
	if x < x_size-1 and lights[x+1, y]:
		number_lights_on_around += 1
	if x > 0 and y < y_size-1 and lights[x-1, y+1]:
		number_lights_on_around += 1
	if y < y_size-1 and lights[x, y+1]:
		number_lights_on_around += 1
	if x < x_size-1 and y < y_size-1 and lights[x+1, y+1]:
		number_lights_on_around += 1

	return number_lights_on_around

def animate(number_iteration, lights, x_size, y_size):
	for i in range(0, number_iteration):
		new_configuration = {}
		for y in range(0, y_size):
			for x in range(0, x_size):
				lit_neighbor = number_lit_neighbor(lights, x, y, x_size, y_size)
				new_configuration[x,y] = switching_rule(lights[x,y], lit_neighbor)

		lights = copy.deepcopy(new_configuration)
	return lights

def animate_corners_stuck(number_iteration, lights, x_size, y_size):
	lights[0,0] = True
	lights[0, y_size-1] = True
	lights[x_size-1, 0] = True
	lights[x_size-1, y_size-1] = True

	for i in range(0, number_iteration):
		new_configuration = {}
		for y in range(0, y_size):
			for x in range(0, x_size):
				if not((x == 0 and y == 0) or (x == 0 and y == y_size-1) or (x == x_size-1 and y == 0) or (x == x_size-1 and y == y_size-1)):
					lit_neighbor = number_lit_neighbor(lights, x, y, x_size, y_size)
					new_configuration[x,y] = switching_rule(lights[x,y], lit_neighbor)
				else:
					new_configuration[x,y] = True

		lights = copy.deepcopy(new_configuration)
	return lights

with open('input.txt') as input_file:
	lights = {}
	x_size = 0
	y_size = 0

	for y, line in enumerate(input_file):
		y_size += 1
		x_size = len(line.rstrip())
		for x, char in enumerate(line.rstrip()):
			lights[x,y] = True if char == '#' else False
	
	print 'The number of lights on after 100 iteration is:', sum(animate(100, lights, x_size, y_size).values())
	print 'The number of lights on after 100 iteration with corners stuck on is:', sum(animate_corners_stuck(100, lights, x_size, y_size).values())