class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # 对象的官方表达
        return f"MyClass(x={self.x}, y={self.y})"


# 创建一个对象
obj = MyClass(1, 2)

# 使用 repr 获取对象的字符串表示形式
obj_repr = repr(obj)

print(obj_repr)  # 输出: MyClass(x=1, y=2)

# 通过 eval 函数重新得到原对象
new_obj = eval(obj_repr)

print(new_obj.x)  # 输出: 1
print(new_obj.y)  # 输出: 2

a = 3
print(repr(a))
