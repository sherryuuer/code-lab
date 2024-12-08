import re

# joke = 'I remixed a remix, it was back to normal.'
# match = re.search('remix',joke)
#
# if match is not None:
#     print('We found a match!')
# else:
#     print('No match found.')
#
# print('The match is',match.group())

# codes = '123abc xyz789 gh12ij'
# code_match = re.search('\d\w+',codes)
#
# print(code_match.group())

test_string = 'The macguffin will arrive on June 21, 2023.'
# 这些括号是用来给group提取值用的
regex = r'(\w+) (\d{1,2}), (\d{4})'

match = re.search(regex, test_string)

print(match.group)
print('Month:', match.group(1))
print('Day:', match.group(2))
print('Year:', match.group(3))
