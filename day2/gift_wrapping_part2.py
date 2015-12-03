#!/usr/bin/python2.7

file = open('input.txt')

length = 0

for line in file:
	dimensions = line.rstrip().split('x')
	dimensions[0] = int(dimensions[0])
	dimensions[1] = int(dimensions[1])
	dimensions[2] = int(dimensions[2])

	area = [0,0,0]
	area[0] = dimensions[0] * dimensions[1]
	area[1] = dimensions[1] * dimensions[2]
	area[2] = dimensions[2] * dimensions[0]

	small_1 = dimensions[0]
	small_2 = dimensions[1]

	if dimensions[2] < small_2:
		if small_2 < small_1:
			small_1 = small_2
		small_2 = dimensions[2]
	elif dimensions[2] < small_1:
		if small_1 < small_2:
			small_2 = small_1
		small_1 = dimensions[2]

	length += small_2 + small_1 + small_2 + small_1
	length += dimensions[0] * dimensions[1] * dimensions[2]

print length