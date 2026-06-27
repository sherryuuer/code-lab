# from functools import reduce


# list1 = [1, 4, 6]
# list2 = ['Sally', 'Jacky', 'Kitty']
# list3 = (2344, 8978, 7364, 9378)


# def func(x, init):
#     print(x, init)
#     return x + init


# print(reduce(func, list3))
# print(list3)

# print(reduce(func, list1))
# print(list1)


from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def func_cap(item):
    return str(item).capitalize()


print(list(map(func_cap, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(tuple(zip(my_strings, my_numbers[::-1])))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def func_fil(score):
    return score > 50


print(list(filter(func_fil, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def func_combine(init, x):
    return init + x


print(reduce(func_combine, my_numbers, reduce(func_combine, scores, 0)))
