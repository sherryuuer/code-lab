places = ['home', 'work', 'New York', 'Pairs']

print('Case sensitive: ')
places.sort()
print(places)

print('Case insensitive: ')
places.sort(key=lambda x: x.lower())
print(places)

print('define class ------')
# define a class to sort


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

print(tools)

tools2 = [
    Tool('drill', 4),
    Tool('sander', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 50),
]

# sort by two key : with truple
# tools2.sort(key=lambda x: (x.name, x.weight))
# print(tools2)
# [Tool('circular saw', 5), Tool('drill', 4), Tool('jackhammer', 50), Tool('sander', 4)]

# 单独对weight取降序排序
# tools2.sort(key=lambda x: (-x.weight, x.name))
# print(tools2)
# [Tool('jackhammer', 50), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]

# 单独对name取降序方向，会返回错误，字符串不支持！
# tools2.sort(key=lambda x: (-x.name, x.weight))
# print(tools2)
# TypeError: bad operand type for unary -: 'str'


# 稳定的排序需要分开写，比如先用name升序，再用weight降序
tools2.sort(key=lambda x: x.name)
print(tools2)
# [Tool('circular saw', 5), Tool('drill', 4), Tool('jackhammer', 50), Tool('sander', 4)]
tools2.sort(key=lambda x: x.weight, reverse=True)
print(tools2)
# [Tool('jackhammer', 50), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]
# 在第一轮中升序的name，在第二轮中就可以保持原有的顺序！
