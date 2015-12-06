#!/usr/bin/python2.7

import re
import numpy

light_matrix = numpy.zeros((1000,1000), dtype= numpy.int)
regex = '^([a-z ]+)(\d+)(?:,)(\d+)(?: \w+ )(\d+)(?:,)(\d+)'

with open('input.txt') as fp:

	for line in fp:
		instructions = re.search(regex, line)

		for x_axis in range(int(instructions.group(2)), int(instructions.group(4))+1):
			for y_axis in range(int(instructions.group(3)), int(instructions.group(5))+1):

				if instructions.group(1) == 'turn on ':
					light_matrix[x_axis, y_axis] = 1
				elif instructions.group(1) == 'turn off ':
					light_matrix[x_axis, y_axis] = 0
				elif instructions.group(1) == 'toggle ':
					light_matrix[x_axis, y_axis] ^= 1

print numpy.count_nonzero(light_matrix)


