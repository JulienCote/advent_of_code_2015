#!/usr/bin/python2.7

file = open('input.txt')
file = file.read()

value = 0
position = 1

for c in file:
	if c == '(':
		value += 1
	elif c == ')':
		value -= 1

	if value == -1:
		print position
		break;
	position +=1
