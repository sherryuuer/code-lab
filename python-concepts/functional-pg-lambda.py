from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda x: str(x).capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(tuple(zip(my_strings, my_numbers[::-1])))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda x: x > 50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(lambda init, x: init + x, my_numbers + scores, 0))


# practice
my_list = [5, 4, 3]
print(list(map(lambda x: x**2, my_list)))

print('---------')
# list sort by second element
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda x: x[1]))
