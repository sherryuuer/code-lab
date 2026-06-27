def fib(num):
    if num <= 1:
        return num
    else:
        for i in range(num):
            return fib(num - 1) + fib(num - 2)


for i in range(21):
    print(fib(i))


def fib2(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for i in fib2(21):
    print(i)
