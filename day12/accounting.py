import re
import json

def sum_all(text):
    regex = '(-?\d+)+'
    numbers = re.findall(regex, text)
    numbers = [int(i) for i in numbers]
    return sum(numbers)

def redless_sum(json_object):
    partial_sum = 0
    for element in json_object:
        if type(element) is dict and u'red' not in element.values():
            partial_sum += redless_sum(element.values())
        elif type(element) is int:
            partial_sum += element
        elif type(element) is list:
            partial_sum += redless_sum(element)
    return partial_sum

with open('input.txt') as input_file:
    input_text = input_file.read()
    json_object = json.loads(input_text)

    print 'sum of all ints: ' + str(sum_all(input_text))
    print 'sum of non-red ints: ' + str(redless_sum(json_object))