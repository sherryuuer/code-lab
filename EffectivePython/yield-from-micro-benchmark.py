import timeit


def child():
    for i in range(1000000):
        yield i


def slow():
    for i in child():
        yield i


# yield from性能胜过在for循环里手工编写生成表达式
def fast():
    yield from child()


baseline = timeit.timeit(
    stmt='for _ in slow(): pass',
    globals=globals(),
    number=50
)
print(f'Manual nesting {baseline:.2f}s')

comparison = timeit.timeit(
    stmt='for _ in fast(): pass',
    globals=globals(),
    number=50
)
print(f'Composed nesting {comparison:.2f}s')

reduction = -(comparison - baseline) / baseline
print(f'{reduction:.1%} less time')
