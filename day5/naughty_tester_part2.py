#!/usr/bin/python2.7

nice_string_counter = 0

with open('input.txt') as fp:

	for line in fp:
		very_previous_char = ''
		previous_char = ''

		pairing_time = 0
		letter_pair = False
		inbetween_repeater = False
		char_pair_record = []

		for char in line:
			if ((previous_char + char) in char_pair_record[:-1]):
				letter_pair = True

			char_pair_record.append(previous_char + char)

			if (very_previous_char == char):
				inbetween_repeater = True


			very_previous_char = previous_char
			previous_char = char
			
		if (letter_pair and inbetween_repeater):
			nice_string_counter += 1

	print nice_string_counter



