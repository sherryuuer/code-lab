import pytest


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11*num == output


# 此处测试将输入乘以 11，并将结果与预期输出进行比较。 测试有 4 组输入，每组有 2 个值——一个是要乘以 11 的数字，另一个是预期结果。

# Pytest -k multiplication -v
