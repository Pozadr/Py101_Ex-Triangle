# Exercise:
# 1) Download the data from user: a, b, c - side of a triangle
# 2) Check if it's possible to draw a triangle and is it rectangular triangle.
# 3) If it is possible count its area and circumference.
#    If it's not print message.

import math  # attach math library

user_decision = 'y'

while user_decision != 'n':
    try:
        triangle_data = input('Type 3 sides of triangle splited with comma: ')

        # tmp_list = []
        # for x in triangle_data.split(','): # split string and write it to the list
        #     tmp_list.append(int(x))  # add component of list
        # a, b, c = tmp_list #  unpack list

        # instead of lines 15-18 an inline list creation
        a, b, c = [int(x) for x in triangle_data.split(',')]
    except ValueError:
        print('Wrong data. Try again.')
        continue
    
    print('\nSides of triangle are a: %s; b: %s; c: %s' % (a, b, c))

    if a + b > c and a + c > b and b + c > a:
        print('With this data you can draw a triangle.')
        # Is triangle the rectangular triangle?
        if (a**2 + b**2 == c**2 or
            a**2 + c**2 == b**2 or
            b**2 + c**2 == a**2):
            print('Triangle is rectangular triangle.')

        print('Circumference: ', (a + b + c))
        p = 0.5 * (a + b + c) # 'p' for Heron equation
        #  Heron equation - count the area of triangle 
        area = math.sqrt(p*(p - a) * (p - b) * (p - c))
        print('Area: ', area)
        user_decision = 'n'
    else:
        print('With this data you cannot draw a triangle.')
        user_decision = input('Wanna try again? (y/n)')
        
print('End of program!')
