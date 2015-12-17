import re
from operator import add
import numpy
import time

ingredients = []

best_taste = -1
best_500_cal = -1

def ingredient_mixer(number_levels, recipee, current_level=0, current_ingredient=0):
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
            ingredient_mixer(number_levels, map(add, ingredient, recipee), current_level+1, ingredients.index(ingredient))

def math_part2():
    max_taste = 0
    for c1 in range(1, 40):
        for c2 in range(1, 60):
            if 5*c1 + c2 < 80 and 3*c1-20 > 0 and c1-5*c2 < 0:
                a = -(c2-60)
                b = c2
                c = -(c1-40)
                d = c1
                
                recipee = [a*x for x in ingredients[0]]
                recipee = map(add, recipee, [b*x for x in ingredients[1]])
                recipee = map(add, recipee, [c*x for x in ingredients[2]])
                recipee = map(add, recipee, [d*x for x in ingredients[3]])

                taste = reduce(lambda x,y:x*y,recipee[:-1])
                if taste > max_taste:
                    max_taste = taste

    return max_taste


with open('input.txt') as input_file:
    for line in input_file:
        split_line = re.search('\w+: \w+ (\d), \w+ (-?\d), \w+ (-?\d), \w+ (-?\d), \w+ (\d)', line)
        ingredients.append([int(split_line.group(1)), int(split_line.group(2)), int(split_line.group(3)), int(split_line.group(4)), int(split_line.group(5))])

    start_time = time.time()

    ingredient_mixer(100, [0 for x in ingredients[0]])
    # ingredient_mixer2(100)

    # print math_part2()

    print("--- %s seconds ---" % (time.time() - start_time))

    print 'Best tasting cookie tastes like: ' + str(best_taste)
    print 'Best 500 cal cookie tastes like: ' + str(best_500_cal)



# #part1
# 2*a > 0
# 5*b - d > 0
# -2*a - 3*b + 5*c >0
# 5*d - c > 0
# a+b+c+d = 100
# a >= 0
# b >= 0
# c >= 0
# d >= 0

# #part 2
# a= -(c2-60)
# b= c2
# c= -(c1-40)
# d= c1
# 5*c1 + c2 < 80
# 3*c1-20 > 0
# c1 - 5*c2 < 0
# 0 < c1 < 40
# 0 < c2 < 60