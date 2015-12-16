import re
from operator import add

ingredients = []

best_taste = 0
best_500_cal = 0

def ingredient_mixer(number_levels, current_level=0, current_ingredient=0, recipee=[0,0,0,0,0]):
    global best_taste
    global best_500_cal

    if current_level == number_levels:
        for i in range(0, 4):
            if recipee[i] < 0:
                recipee[i] = 0

        taste = reduce(lambda x,y:x*y,recipee[:-1])

        if recipee[4] == 500 and best_500_cal < taste:
            best_500_cal = taste
        if best_taste < taste:
            best_taste = taste
    else:
        for ingredient in ingredients[current_ingredient:]:
            ingredient_mixer(number_levels, current_level+1, ingredients.index(ingredient), map(add, ingredient, recipee))

with open('input.txt') as input_file:
    for line in input_file:
        split_line = re.search('\w+: \w+ (\d), \w+ (-?\d), \w+ (-?\d), \w+ (-?\d), \w+ (\d)', line)
        ingredients.append([int(split_line.group(1)), int(split_line.group(2)), int(split_line.group(3)), int(split_line.group(4)), int(split_line.group(5))])

    ingredient_mixer(100)

    print 'Best tasting cookie tastes like: ' + str(best_taste)
    print 'Best 500 cal cookie tastes like: ' + str(best_500_cal)
