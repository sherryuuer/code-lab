# pytest test_fixture.py -s 显示详细信息
# 在 Pytest 中，`fixture` 是一种功能强大的机制，用于管理测试中的资源、设置和数据。它允许你在测试函数中定义和使用可复用的代码块。

### 基本用法：

# 1. 定义Fixture

# import pytest

# @pytest.fixture
# def setup_and_teardown():
#     # Setup code
#     print("Setup")
    
#     # Yield the control back to the test
#     yield

#     # Teardown code
#     print("Teardown")

# # 2. 在测试函数中使用 Fixture

# def test_example(setup_and_teardown):
#     print("Test logic goes here")


# 在这个例子中，`setup_and_teardown` 是一个被用作 `fixture` 的函数。当 `test_example` 函数被执行时，`setup_and_teardown` 的内容会在测试之前（setup）和测试之后（teardown）执行。

# 2. 传递参数：

# import pytest

# @pytest.fixture
# def setup_and_teardown(request):
#     # Setup code
#     print("Setup")

#     # Access the test function name
#     print(f"Running test: {request.node.name}")

#     # Yield the control back to the test
#     yield

#     # Teardown code
#     print("Teardown")

# def test_example(setup_and_teardown):
#     print("Test logic goes here")

# 在这个例子中，`request` 参数允许你访问测试函数的一些属性，如函数名等。

# 3. 多个 Fixture：

# 可以同时使用多个 `fixture`，并在测试函数中按照需要进行组合：

import pytest

@pytest.fixture
def setup():
    print("Setup")
    yield
    print("Teardown")

@pytest.fixture
def data():
    return {"key": "value"}

def test_example(setup, data):
    print("Test logic goes here")
    print(f"Data: {data}")


# `test_example` 函数同时使用了 `setup` 和 `data` 两个 `fixture`。

