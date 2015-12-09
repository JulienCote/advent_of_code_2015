#!/usr/bin/python2.7

file = open('input.txt')

x = [0, 0]
y = [0, 0]
santa_vs_robot = 0
record = []

file = file.read()

for c in file:
	if [x[santa_vs_robot], y[santa_vs_robot]] not in record:
		record.append([x[santa_vs_robot], y[santa_vs_robot]])

	if c == '^':
		y[santa_vs_robot] += 1
	elif c == '>':
		x[santa_vs_robot] += 1
	elif c == '<':
		x[santa_vs_robot] -= 1
	elif c == 'v':
		y[santa_vs_robot] -= 1

	santa_vs_robot = ~santa_vs_robot

print len(record)