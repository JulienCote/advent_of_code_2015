#!/usr/bin/python2.7

input_sequence = '1113222113'

for i in range(0,50):
    same_char_count = 1
    previous_character = input_sequence[0]
    input_sequence = input_sequence[1:]
    next_sequence = ''

    for character in input_sequence:
        if character == previous_character:
              same_char_count += 1
        else:
            next_sequence += str(same_char_count) + previous_character
            same_char_count = 1
            previous_character = character

    next_sequence += str(same_char_count) + previous_character
    input_sequence = next_sequence

print len(input_sequence)
