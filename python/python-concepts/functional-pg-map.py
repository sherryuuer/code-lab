# map()
my_list = [1, 2, 4]


def mutiply_by2_org(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return new_list


print(mutiply_by2_org(my_list))

def mutiply_by2(item):
    return item*2


print(list(map(mutiply_by2, my_list)))
print(my_list)

# output
# [2, 4, 8]
# [1, 2, 4]
