# bubble sort
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


names = ['pretizels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)


# emunerate
snacks = [('bacon', 350), ('donut', 240), ('muffin', 290)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'{rank}: {name} has {calories} calories.')


# these are all Pythonic
# unpacking list
car_ages = [0, 13, 2, 5, 4, 45, 6,]
car_ages_sorted = sorted(car_ages, reverse=True)
print(car_ages_sorted)
oldest, *others, youngest = car_ages_sorted
print(oldest, youngest)

# generator


def generator_cats():
    yield 'Kitty1'
    yield 'Kitty2'
    yield 'Kitty3'
    yield 'Kitty4'


it = list(generator_cats())  # not need to be list
it = generator_cats()
print(it)
kitty, *others = it
print(kitty)
