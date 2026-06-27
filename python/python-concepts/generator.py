def generator_func(num):
    for i in range(num):
        yield i


g = generator_func(1000)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterable)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])
