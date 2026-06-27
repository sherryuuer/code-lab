# Define the time checker.
from time import time


def time_checker(func):
    def wrap_func(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        over_time = time()
        run_time = over_time - start_time
        return f"Run by time {run_time}", res
    return wrap_func


@time_checker
def long_time():
    a = 1
    for i in range(100000):
        a += i * 2
    # print("give me a", a)
    return a


a = long_time()  # a 现在是wrap_func所以不输出里面的结果
print(a, "??")
