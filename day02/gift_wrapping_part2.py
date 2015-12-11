#!/usr/bin/python2.7

file = open('input.txt')

length = 0

for line in file:
	dimensions = line.rstrip().split('x')
	dimensions[0] = int(dimensions[0])
	dimensions[1] = int(dimensions[1])
	dimensions[2] = int(dimensions[2])

	dimensions.sort()

	length += (dimension[0] + dimensions[1]) * 2
	length += dimensions[0] * dimensions[1] * dimensions[2]

print length
