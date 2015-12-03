#!/usr/bin/python2.7

file = open('input.txt')

position = [[0,0], [0,0]]
santa_vs_robot = 0
record = []

file = file.read()

def position_to_string():
	return str(position[santa_vs_robot][0]) + '.' + str(position[santa_vs_robot][1])

for c in file:
	if position_to_string() not in record:
		record.append(position_to_string())

	if c == '^':
		position[santa_vs_robot][1] += 1
	elif c == '>':
		position[santa_vs_robot][0] += 1
	elif c == '<':
		position[santa_vs_robot][0] -= 1
	elif c == 'v':
		position[santa_vs_robot][1] -= 1

	santa_vs_robot  = santa_vs_robot ^ 1

print len(record)