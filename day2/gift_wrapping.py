#!/usr/bin/python2.7

file = open('input.txt')

length = 0

for line in file:
	dimensions = line.rstrip().split('x')
	area = [0,0,0]
	area[0] = int(dimensions[0]) * int(dimensions[1])
	area[1] = int(dimensions[1]) * int(dimensions[2])
	area[2] = int(dimensions[2]) * int(dimensions[0])

	length += min(area[0], area[1], area[2])
	length += area[0] * 2 + area[1] * 2 + area[2] * 2

print length