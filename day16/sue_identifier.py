import re

right_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

with open('input.txt') as input_file:
    have_part1 = False
    have_part2 = False
    for line in input_file:
        split_line = re.search('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)

        if not have_part1 and right_sue[split_line.group(2)] == int(split_line.group(3)) and right_sue[split_line.group(4)] == int(split_line.group(5)) and right_sue[split_line.group(6)] == int(split_line.group(7)):
            print 'The right part1 sue is number: ' + split_line.group(1)
            have_part1 = True

        if not have_part2:
            have_wrong_bit = False
            for i in range(2, 7, 2):
                if split_line.group(i) in ['cats', 'trees']:
                    if not right_sue[split_line.group(i)] < int(split_line.group(i+1)):
                        have_wrong_bit = True
                elif split_line.group(i) in ['pomeranians', 'goldfish']:
                    if not right_sue[split_line.group(i)] > int(split_line.group(i+1)):
                        have_wrong_bit = True
                else:
                    if right_sue[split_line.group(i)] != int(split_line.group(i+1)):
                        have_wrong_bit = True

            if not have_wrong_bit:
                print 'The right part2 sue is number: ' + split_line.group(1)
                have_part2 = True

        if have_part1 and have_part2:
            break