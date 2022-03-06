import math


def my_log(l):
    return [math.log(num) if num > 0 else None for num in l]


print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))
