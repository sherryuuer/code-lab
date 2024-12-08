import re


text = 'The cat and the dog are friends.'
regex = 'cat|dog'
matches = re.findall(regex, text)
# print(matches)


regex = r'((June|July) \d{1,2})'  # 这里的括号是必须的，必然匹配的就是六月，或者七月+日期
text = 'I will be on vacation from June 28 through July 2.'
matches = re.findall(regex, text)
# print(matches)


regex = r'(\d{1,2}(-|/)\d{1,2}(-|/)\d{4})'
text = 'I will be on vacation from 06-28-2023 through 07/02/2023.'
matches = re.findall(regex, text)
print(matches)
print(matches[0][0], matches[1][0])
