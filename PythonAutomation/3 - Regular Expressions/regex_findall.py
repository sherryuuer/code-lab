import re

text = 'The World Cup of 1998 was hosted by France. The next edition in 2002 was hosted by South Korea and Japan. The most recent one in 2022 took place in Qatar.'
regex = r'\d{4}'

years = re.findall(regex, text)
print(years)


text = 'The cat goes meow, meooooow, meoooow, meowwwww, while the dog goes woof.'
regex = r'meo+w+'

sounds = re.findall(regex, text)
print(sounds)
# 返回一个列表
