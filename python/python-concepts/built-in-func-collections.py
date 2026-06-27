# `collections` 模块是 Python 标准库中提供的一个模块，用于提供额外的数据结构和工具，扩展了内置的数据类型。以下是一些常见的 `collections` 模块中数据结构的例子：

# 1. **Counter:**
#    `Counter` 是一个字典的子类，用于计算可迭代对象中元素的出现次数。

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

# 创建 Counter 对象
word_counts = Counter(
    ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

# 获取元素出现次数
print(word_counts['apple'])  # 输出 3


# 2. **defaultdict:**
#    `defaultdict` 是一个字典的子类，它接受一个工厂函数作为默认值的来源。


# 创建 defaultdict 对象
fruit_dict = defaultdict(int)

# 使用 defaultdict 计数
fruit_dict['apple'] += 1
fruit_dict['banana'] += 2

print(fruit_dict)  # 输出 defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})

# 3. **deque:**
#    `deque` 是一个双端队列，支持在两端高效地进行添加和弹出操作。


# 创建 deque 对象
my_queue = deque([1, 2, 3])

# 在队列两端进行操作
my_queue.append(4)  # 添加到右侧
my_queue.appendleft(0)  # 添加到左侧

print(my_queue)  # 输出 deque([0, 1, 2, 3, 4])

# 4. **namedtuple:**
#    `namedtuple` 是一个工厂函数，用于创建带有字段名称的元组。


# 创建 namedtuple 类型
Point = namedtuple('Point', ['x', 'y'])

# 创建 namedtuple 对象
p = Point(1, 2)

print(p.x, p.y)  # 输出 1 2
print(p)  # Point(x=1, y=2)
