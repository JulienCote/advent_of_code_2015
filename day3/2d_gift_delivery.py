#!/usr/bin/python2.7

file = open('input.txt')

x = 0
y = 0
record = []

file = file.read()

for c in file:
	if [x,y] not in record:
		record.append([x,y])
		
	if c == '^':
		y += 1
	elif c == '>':
		x += 1
	elif c == '<':
		x -= 1
	elif c == 'v':
		y -= 1

print len(record)