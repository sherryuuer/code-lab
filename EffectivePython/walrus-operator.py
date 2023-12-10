# :=
# 赋值表达式
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


def make_lemonade(count):
    pass


def out_of_stock():
    pass


count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# use walrus operator
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

# if need 4 apples
if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_lemonade(count)
else:
    out_of_stock()


# like switch case:
def slice_banana(count):
    pass


def make_smoothies(count):
    pass


def make_cider(count):
    pass


if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_banana(count)
    to_enjoy = make_smoothies(piece)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('lemon', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

# like do while:


def pick_fruit():
    pass


def make_juice(fruit, count):
    pass


bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
