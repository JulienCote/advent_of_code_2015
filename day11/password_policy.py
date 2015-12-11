#!/usr/bin/python2.7

input_sequence = 'hepxcrrq'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def string_to_value_password(password):
    value = []
    for char in password:
        value.append(alphabet.index(char))
    return value

def value_password_to_string(values):
    password = ''
    for value in values:
        password += alphabet[value]
    return password

#will not work if length of password increases
def increment_password_value(values, value_index=1):
    if value_index >= len(values):
        print values
    values[-value_index] += 1
    if values[-value_index] == alphabet.index('i') or values[-value_index] == alphabet.index('o') or values[-value_index] == alphabet.index('l'):
        values[-value_index] += 1
    elif values[-value_index] == 26:
        values[-value_index] %= 26
        values = increment_password_value(values, value_index+1)
    return values

def password_validity_test(password, values):
    # if any(c in ['i', 'o', 'l'] for c in password):
    #     return False

    double_letter_count = 0
    previous_pair_index = -1
    have_increasing_straight = False

    very_previous_letter = password[0]
    previous_letter = password[1]

    if previous_letter == very_previous_letter:
        double_letter_count += 1
        previous_pair_index = 1

    index = 2
    for letter in password[2:]:
        if letter == previous_letter and index - previous_pair_index > 1:
            double_letter_count += 1
            previous_pair_index = index
        if alphabet.index(letter) - alphabet.index(previous_letter) == 1 and alphabet.index(previous_letter) - alphabet.index(very_previous_letter) == 1:
            have_increasing_straight = True

        very_previous_letter = previous_letter
        previous_letter = letter
        index += 1

    return have_increasing_straight and double_letter_count >= 2


def find_next_password(password):
    coded_password = string_to_value_password(password)
    coded_password = increment_password_value(coded_password)

    while(not password_validity_test(value_password_to_string(coded_password), coded_password)):
        coded_password = increment_password_value(coded_password)

    return value_password_to_string(coded_password)

if __name__  == "__main__":
    new_password = find_next_password(input_sequence)
    print 'new password is: ' + new_password
    new_password = find_next_password(new_password)
    print 'and the one after is: ' + new_password