present_target = 33100000

def find_min_house(present_count):
	for index, count in enumerate(present_count):
		if count >= present_target:
			return index

def infinite_deliveries():
	present_count = [0 for x in range(0, present_target / 10)]
	for i in range(1, present_target/10):
		for j in range(i, present_target/10, i):
			present_count[j] += i * 10

	print 'The house id for infinite deliveries is :', find_min_house(present_count)

def max_50_deliveries():
	present_count = [0 for x in range(0, present_target / 11)]

	for i in range(1, present_target / 11):
		delivery_count = 0
		for j in range(i, present_target / 11, i):
			present_count[j] += i * 11
			delivery_count += 1
			if delivery_count == 50:
				break

	print 'The house id for 50 max deliveries is :', find_min_house(present_count)


infinite_deliveries()

max_50_deliveries()