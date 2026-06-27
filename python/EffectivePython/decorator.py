# from 26
# functools.wraps可以定义函数修饰
# 比如定义对一个函数的参数进行跟踪的装饰器
from functools import wraps


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


@trace
def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


res = fibonacci(8)
print(res)

print(fibonacci)
# 返回的并不是我们想要的函数的名字
# <function trace.<locals>.wrapper at 0x103130d60>
# 使用functools的内置模块wraps可以解决这个问题
# wraps本身也是个修饰器，它可以帮助你编写自己的修饰器。把它运用到wrapper函数上面，它就会将重要的元数据（metadata）全都从内部函数复制到外部函数。


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


@trace
def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


res = fibonacci(8)
print(res)
print(fibonacci)
# 现在就正常了
# <function fibonacci at 0x100dbbc40>
