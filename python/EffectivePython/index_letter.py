# from 30
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
        print(result)
    return result


address = 'four score and seven years age, I get a cow.'
result = index_words(address)
print(result[:6])
# 有趣！遇到字母不add，直到空格就加入下一个index！


# 使用迭代器更高效和节省内存
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


it = index_words_iter(address)
print(next(it))
print(next(it))


# 如果要制作列表也可以
res = list(index_words_iter(address))
print(res[:6])
