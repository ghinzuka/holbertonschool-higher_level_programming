#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    divide = 0
    if not my_list:
        return 0
    else:
        for (x, y) in my_list:
            weight += x * y
            divide += y
        return weight / divide
