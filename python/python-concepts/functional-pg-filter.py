my_list = [2, 5, 7, 8]


def check_odd(item):
    return item % 2 != 0
# odd奇数，even偶数


print(list(filter(check_odd, my_list)))
print(my_list)
