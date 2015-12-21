from itertools import combinations
containers = []

with open('input.txt') as input_file:
    for line in input_file:
        containers.append(int(line))

    number_combination = 0
    smallest_number = -1

    for i in range(1, len(containers)):
        if i == smallest_number + 1:
            print number_combination
        for combination in combinations(containers, i):
            if sum(combination) == 150:
                if smallest_number == -1:
                    smallest_number = i
                number_combination += 1

    print number_combination