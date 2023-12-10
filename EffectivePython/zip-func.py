# if have two iterator, use zip
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

# find the longest
longest_name = None
max_count = 0
# if use enumerate
for i, name in enumerate(names):
    if len(name) > max_count:
        longest_name = name
        max_count = len(name)

print(longest_name, max_count)

# if use zip
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name, max_count)

# 我觉得前提是真的是两个分开的列表配对的时候用zip，这个例子其实enumerate也不错
# 列表不一样长遵循短的
# zip_longest function in itertools package
