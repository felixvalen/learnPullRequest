#!/usr/bin/python3

import random

def randomFood():
    name = input('Hi! Enter your name :')
    food = ['pizza', 'cookies', 'paella', 'bread', 'patatas']
    num = random.randint(0, len(food) - 1)
    selectedFood = food[num]
    return "{}, today, you have to eat {}".format(name,selectedFood )



print(randomFood())