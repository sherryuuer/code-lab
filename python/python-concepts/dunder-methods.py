# 当你自定义一个类时，可以通过添加特殊方法来定制该类的行为。下面是一个简单的示例，演示如何自定义一个类，并实现其中的一些特殊方法：


class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"MyVector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, MyVector):
            return MyVector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add two MyVector instances.")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# 创建两个 MyVector 实例
v1 = MyVector(1, 2)
v2 = MyVector(3, 4)

# 使用特殊方法
print(v1)               # 调用 __str__ 方法
v3 = v1 + v2           # 调用 __add__ 方法
print(v3)               # 输出 MyVector(4, 6)
print(v1 == v2)         # 调用 __eq__ 方法，输出 False
print(v1 == MyVector(1, 2))  # 输出 True


# 在这个示例中，我们定义了一个名为`MyVector`的类，它代表二维向量。我们自定义了`__init__`构造方法来初始化向量的坐标，`__str__`方法来返回向量的字符串表示，`__add__`方法来实现向量的加法操作，以及`__eq__`方法来比较两个向量是否相等。

# 通过自定义这些特殊方法，我们可以使用自定义的类更自然地执行操作，例如在向量上执行加法操作，比较向量是否相等，以及以更可读的方式输出向量的信息。
