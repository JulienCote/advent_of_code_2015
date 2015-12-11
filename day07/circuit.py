#!/usr/bin/python2.7

gates = []
wires = {}

class Gate:
	def __init__(self, input_wire, output_wire, gate_type):
		self.input_wire = input_wire
		self.output_wire = output_wire
		self.type = gate_type

	def __repr__(self):
		return str([self.input_wire, self.output_wire, self.type])

	def compute_value(self):
		if(self.output_wire in wires) :
			return wires[self.output_wire]

		if self.type == 'signal':
			value =  self.input_wire
		elif self.type == 'redirect':
			for gate in gates:
				if gate.output_wire == self.input_wire:
					value =  gate.compute_value()

		elif self.type == 'NOT':
			for gate in gates:
				if gate.output_wire == self.input_wire:
					value = ~gate.compute_value()

		elif self.type == 'OR':
			gate_inputs = []
			for gate in gates:
				if gate.output_wire in self.input_wire:
					gate_inputs.append(gate)					
			if len(gate_inputs) == 1:
				value = (self.input_wire[0] | gate_inputs[0].compute_value())
			else:
				value = (gate_inputs[0].compute_value() | gate_inputs[1].compute_value())
			
		elif self.type == 'AND':
			gate_inputs = []
			for gate in gates:
				if gate.output_wire in self.input_wire:
					gate_inputs.append(gate)
			if len(gate_inputs) == 1:
				value = (int(self.input_wire[0]) & gate_inputs[0].compute_value())
			else:
				value = (gate_inputs[0].compute_value() & gate_inputs[1].compute_value())

		elif self.type == 'LSHIFT':
			for gate in gates:
				if gate.output_wire == self.input_wire[0]:
					value = (gate.compute_value() << int(self.input_wire[1]))

		elif self.type == 'RSHIFT':
			for gate in gates:
				if gate.output_wire == self.input_wire[0]:
					value = (gate.compute_value() >> int(self.input_wire[1]))

		wires[self.output_wire] = value;
		return value

with open('input.txt') as input_file:
	for line in input_file:
		split_line = line.rstrip('\n').split(' ')

		if(split_line[0] == 'NOT'):
			input_wire = ()
			output_wire = ()

			new_gate = Gate(split_line[1], split_line[3], split_line[0])
			gates.append(new_gate)
		elif (split_line[0].isdigit() and len(split_line) == 3):
			new_gate = Gate(int(split_line[0]), split_line[2], 'signal')
			gates.append(new_gate)
		else:
			if len(split_line) == 3:
				new_gate = Gate(split_line[0], split_line[2], 'redirect')
				gates.append(new_gate)
			else:
				new_gate = Gate([split_line[0], split_line[2]], split_line[4], split_line[1])
				gates.append(new_gate)

first_part_answer = 0
second_part_answer = 0

for gate in gates:
	if gate.output_wire == 'a':
		output_gate = gate
		first_part_answer = gate.compute_value()

wires = {}
wires['b'] = first_part_answer

second_part_answer = output_gate.compute_value()

print 'first part: ' + str(first_part_answer)
print 'second part: ' + str(second_part_answer)