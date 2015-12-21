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



with open('input.txt') as input_file:
	transformaition_regex = '(\w+) => (\w+)'
	molecule_regex = '([A-Z][a-z]?)'
	transformations = {}

	for line in input_file:
		split = re.match(transformaition_regex, line)
		if split:
			if split.group(1) in transformations:
				transformations[split.group(1)].append(split.group(2))
			else:
				transformations[split.group(1)] = [split.group(2)]
		else:
			if line != '\n':
				initial_molecule = line.rstrip()

	atoms_in_molecule = re.findall(molecule_regex, initial_molecule)

	print len(set(replace_single_molecule(atoms_in_molecule, transformations)))