#!/usr/bin/python2.7

file = open('input.txt')

position = [0,0]
record = []

file = file.read()

def position_to_string():
	return str(position[0]) + '.' + str(position[1])

for c in file:
	if position_to_string() not in record:
		record.append(position_to_string())
		
	if c == '^':
		position[1] += 1
	elif c == '>':
		position[0] += 1
	elif c == '<':
		position[0] -= 1
	elif c == 'v':
		position[1] -= 1

print len(record)