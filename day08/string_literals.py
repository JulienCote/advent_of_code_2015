#!/usr/bin/python2.7

import re

char_count = 0
memory_count = 0
encoded_count = 0

with open('input.txt') as input_file:
	for line in input_file:
		line = line.rstrip()
		char_count += len(line)

		decoded = line.decode('string_escape')
		memory_count += len(decoded) - 2

		encoded = re.escape(line)
		encoded_count += len(encoded) + 2


print 'first part: ' + str(char_count - memory_count)
print 'second part: ' + str(encoded_count - char_count)