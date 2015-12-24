import re

def half(register):
	return register // 2

def triple(register):
	return register * 3

def increment(register):
	return register + 1

def jump(offset, pp):
	return pp + offset

def jump_if_even(register, offset, pp):
	if register % 2 == 0:
		return pp + offset
	return pp + 1

def jump_if_one(register, offset, pp):
	if register == 1:
		return pp + offset
	return pp + 1

def run(registers, instructions):
	pp = 0
	while pp in range(0, len(instructions)):
		if instructions[pp][0] == 'hlf':
			registers[instructions[pp][1]] = half(registers[instructions[pp][1]])
			pp += 1
		elif instructions[pp][0] == 'tpl':
			registers[instructions[pp][1]] = triple(registers[instructions[pp][1]])
			pp += 1
		elif instructions[pp][0] == 'inc':
			registers[instructions[pp][1]] = increment(registers[instructions[pp][1]])
			pp += 1
		elif instructions[pp][0] == 'jmp':
			pp = jump(instructions[pp][1], pp)
		elif instructions[pp][0] == 'jie':
			pp = jump_if_even(registers[instructions[pp][1]], instructions[pp][2], pp)
		elif instructions[pp][0] == 'jio':
			pp = jump_if_one(registers[instructions[pp][1]], instructions[pp][2], pp)

	return registers

with open('input.txt') as input_file:
	instructions = []
	for line in input_file:
		split = re.search('(\w+) (\w|[\+-]\d+),? ?([\+-]\d+)?', line)
		if split.group(1) == 'hlf' or split.group(1) == 'tpl' or split.group(1) == 'inc':
			instructions.append([split.group(1), split.group(2)])
		elif split.group(1) == 'jmp':
			instructions.append([split.group(1), int(split.group(2))])
		elif split.group(1) == 'jie' or split.group(1) == 'jio':
			instructions.append([split.group(1), split.group(2), int(split.group(3))])

	registers = {'a':0, 'b':0}
	print 'The value of register b after execution is when a=0: ', run(registers, instructions)['b']
	registers = {'a':1, 'b':0}
	print 'The value of register b after execution is when a=1: ', run(registers, instructions)['b']

	