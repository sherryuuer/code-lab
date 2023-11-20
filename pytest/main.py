# import pytest

# pip install pytest
# pip list

# pytest -vv test_func.py
# pytest # run all


# 在不指定文件名的情况下运行 pytest 将运行当前目录和子目录中格式为 test_*.py 或 *_test.py 的所有文件。 Pytest 自动将这些文件识别为测试文件。 我们可以通过明确提及它们来使 pytest 运行其他文件名。

# pytest -v

# -k <substring> 表示要在测试名称中搜索的子字符串。
# pytest -k great -v
# 这里是包含了great的测试会被测试

# 分组测试
# 标记mark，在代码的函数上用修饰符
# pytest -m <markername> -v
# eg. pytest -m others -v


# 可以在此文件中定义 fixture 函数，使它们可以跨多个测试文件访问。conftest.py
# fixture(夹具)是函数，将在应用它的每个测试函数之前运行。 fixture(夹具)用于向测试提供一些数据，例如数据库连接、要测试的 URL 和某种输入数据。 因此，我们可以将 fixture 函数附加到测试，而不是为每个测试运行相同的代码，它会在执行每个测试之前运行并将数据返回给测试。
# pytest -k divisible -v


# 参数化测试
# Pytest -k multiplication -v


# Pytest 中的 Skip 和 Xfail 测试,选择让测试失败或跳过测试
# @pytest.mark.xfail
# @pytest.mark.skip

# pytest test_compare.py -v

# 在 n 次测试失败后立即停止执行测试套件的语法
# pytest --maxfail = <num>
# pytest test_failure.py -v --maxfail 1


# 并行测试
# 需要先安装 pytest-xdist 插件
# pip install pytest-xdist

# pytest -n 3
# -n <num> 使用多个 worker 运行测试，这里是 3 个。


# 从 test_multiplcation.py 执行测试并通过运行生成 xml测试结果
# pytest test_multiplication.py -v --junitxml="result.xml"
