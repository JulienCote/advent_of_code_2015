#!/usr/bin/python2.7

nice_string_counter = 0

with open('input.txt') as fp:

	for line in fp:
		previous_char = ''
		vowel_count = 0
		double_char = False
		evil_chars = False

		for char in line:
			last_2_char = previous_char + char

			if ((last_2_char == 'ab') or (last_2_char == 'cd') or (last_2_char == 'pq') or (last_2_char == 'xy')):
				evil_chars = True
			if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
				vowel_count += 1
			if char == previous_char:
				double_char = True

			previous_char = char

		if (double_char and vowel_count >= 3 and not evil_chars):
			nice_string_counter += 1
			
	print nice_string_counter



