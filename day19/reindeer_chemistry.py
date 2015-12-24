import re

def complete_string_molecule(atoms_in_molecule, index, molecule):
	for i in range(index+1, len(atoms_in_molecule)):
		molecule += atoms_in_molecule[i]
	return molecule


def replace_single_molecule(atoms_in_molecule, transformations):
	molecule = ''
	transformed_molecules = []

	for i in range(0, len(atoms_in_molecule)):
		if atoms_in_molecule[i] in transformations:
			for transformation in transformations[atoms_in_molecule[i]]:
				transformed_molecules.append(complete_string_molecule(atoms_in_molecule, i, molecule + transformation))
			molecule += atoms_in_molecule[i]
		else:
			molecule += atoms_in_molecule[i]
	return transformed_molecules

def deconstruct_molecule(molecule, sorted_keys, reverse_transformations, step=0):
	if molecule == 'e':
		return step

	for key in sorted_keys:
		if key in molecule:
			for option in reverse_transformations[key]:
				return deconstruct_molecule(molecule.replace(key, option, 1), sorted_keys, reverse_transformations, step + 1)


with open('input.txt') as input_file:
	transformaition_regex = '(\w+) => (\w+)'
	molecule_regex = '([A-Z][a-z]?)'
	transformations = {}
	reverse_transformations = {}

	for line in input_file:
		split = re.match(transformaition_regex, line)
		if split:
			if split.group(1) in transformations:
				transformations[split.group(1)].append(split.group(2))
			else:
				transformations[split.group(1)] = [split.group(2)]
			if split.group(2) in reverse_transformations:
				reverse_transformations[split.group(2)].append(split.group(1))
			else:
				reverse_transformations[split.group(2)] = [split.group(1)]
		else:
			if line != '\n':
				initial_molecule = line.rstrip()

	atoms_in_molecule = re.findall(molecule_regex, initial_molecule)

	print 'There are this many new molecules to be possibly made after 1 step:', len(set(replace_single_molecule(atoms_in_molecule, transformations)))

	print 'It will take this many steps to go from "e" to the target molecule:', deconstruct_molecule(initial_molecule, sorted(reverse_transformations.keys(), key=len, reverse=True), reverse_transformations)