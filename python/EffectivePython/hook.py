# from 38
# 挂钩函数
from collections import defaultdict


def log_missing():
    print('key added.')
    return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 7),
    ('orange', 11),
]
# 当值不存在的时候，就会用hook函数log_missing
result = defaultdict(log_missing, current)
print(result)

for key, amount in increments:
    result[key] += amount

print(result)
