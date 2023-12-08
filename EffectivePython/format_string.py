a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')
# ^20s 是字符串格式化符号，表示将字符串 b 左对齐，宽度为 20 个字符。如果字符串 b 的长度小于 20 个字符，则会在左侧填充空格。如果字符串 b 的长度大于 20 个字符，则只会显示前 20 个字符。
print(len(formatted))  # 20


key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

# best! f-string python3.6
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)
formatted = f'{key:<10} = {value:.2f}'
print(formatted)


places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')  # better than hard coding.
