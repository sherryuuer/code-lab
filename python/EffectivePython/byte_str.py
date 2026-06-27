a = b'h\x6511o'
# byte ascii
print(list(a))
print(a)
# b'hello'


# str Unicode
a = 'a\u0300 propos'
print(list(a))
print(a)

# str encode -> bytes
# bytes decode -> str
# helper function


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of str


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of bytes


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


# 可以用加号连接相同类型的字符，不同的不能连接也不能比较
print(b'one' + b'two')  # b'onetwo'
print(b'foo' == 'foo')  # false


print(b'red %s' % b'blue')

# read bytes files
with open('data.bin', 'rb') as f:
    data = f.read()
assert data == b'\xf1\xf2\xf3\xf4\xf5'

with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read()
