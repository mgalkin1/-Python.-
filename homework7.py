import random


def print_params(first, second):
    coordinats = [123, 254, 32134, 4124, 5645, 6754]
    place1 = random.choice(coordinats)
    coordinats.remove(place1)
    place2 = random.choice(coordinats)
    print('first', 'second')
    return place1, place2


place1, place2 = print_params('first', 'second')
print(place1, place2)
