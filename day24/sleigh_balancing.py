import copy
passenger_configuration = []

def choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def make_sleigh_group(remaining_packages, target_weight, current_weight=0, packages=[]):
	global passenger_configuration
	if current_weight > target_weight or (len(packages) > len(passenger_configuration) and len(passenger_configuration) > 0):
		return
	elif target_weight == current_weight:
		if len(passenger_configuration) == 0:
			passenger_configuration = copy.deepcopy(packages)
		elif len(packages) < len(passenger_configuration):
			passenger_configuration = copy.deepcopy(packages)
		elif len(packages) == len(passenger_configuration):
			if reduce(lambda x,y: x*y, passenger_configuration) > reduce(lambda x,y: x*y, packages):
				passenger_configuration = copy.deepcopy(packages)
		return

	for i in range(0, len(remaining_packages)):
		make_sleigh_group(remaining_packages[i+1:len(remaining_packages)], target_weight, current_weight + remaining_packages[i], packages + [remaining_packages[i]])


with open('input.txt') as input_file:
	packages = []
	for line in input_file:
		packages.append(int(line))

	packages.sort(reverse=True)

	make_sleigh_group(copy.deepcopy(packages), sum(packages)/3)

	print 'the entanglement of the passenger seat for 3 groups is:', reduce(lambda x,y: x*y, passenger_configuration)

	passenger_configuration = []
	make_sleigh_group(copy.deepcopy(packages), sum(packages)/4)

	print 'the entanglement of the passenger seat for 4 groups is: ', reduce(lambda x,y: x*y, passenger_configuration)