from collections import defaultdict

# 创建一个默认值为int类型的defaultdict
default_dict_example = defaultdict(int)

# 访问不存在的键，会使用默认值0，并将该键加入字典
default_dict_example['a'] += 1
default_dict_example['b'] += 2

print(default_dict_example)  # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 2})


# defaultdict 允许用户在创建字典时指定默认值的类型，当字典中某个键第一次被访问时，如果该键不存在，defaultdict 会为该键设置一个默认值，并返回这个默认值。

# 通常，我们使用 dict 类创建一个字典时，如果要访问一个不存在的键，会抛出 KeyError 异常。而使用 defaultdict，可以避免这个问题，因为它会自动为不存在的键设置默认值。
