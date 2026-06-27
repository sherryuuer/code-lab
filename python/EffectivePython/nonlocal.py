# from 21
# a sort function,if num is in group, it will be put at front part.
def sort_priority(values, groups):
    def helper(x):
        if x in groups:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


# if add a variable found
# found!!!is not in helper, can not be accessed
def sort_priority(values, groups):
    found = False  # 外层作用域

    def helper(x):
        if x in groups:
            found = True  # seems simple 但是这是helper函数作用域
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found
# vscode显示是灰色的说明拿不到的


# add nonlocal
def sort_priority(values, groups):
    found = False  # 外层作用域

    def helper(x):
        nonlocal found  # nonlocal
        if x in groups:
            found = True  # seems simple 但是这是helper函数作用域
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found


# 一个更好的方法是用类来封装不容易出错
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):   # 这个方法让 实例 可以像函数一样被调用
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)  # 这里的排序方法是先按照0排序再按照第二个


numbers = [2, 5, 5, 6, 7, 0]
groups = {5, 6}
sorter = Sorter(groups)
numbers.sort(key=sorter)
assert sorter.found is True
