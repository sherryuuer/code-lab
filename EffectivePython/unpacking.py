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
