#!/usr/bin/python2.7

file = open('input.txt')
file = file.read()

value = 0

for c in file:
	if c == '(':
		value += 1
	elif c == ')':
		value -= 1

print value
