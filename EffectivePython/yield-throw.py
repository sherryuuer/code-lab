# 35
# code一下在意的地方


def MyError(Exception):
    pass


def my_generator():
    yield 1

    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3

    yield 4


it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))
