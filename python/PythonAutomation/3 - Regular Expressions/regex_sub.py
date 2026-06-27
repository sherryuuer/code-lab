import re

text = 'Contact us at info@example.com or support@mywebsite.com.'
pattern = r'\w+@'

anonymized_text = re.sub(pattern, 'user@', text)

print(anonymized_text)


text = 'The event will take place on 02/14/2024. Please purchase tickets by 01/01/2024.'
pattern = r'(\d{2})/(\d{2})/(\d{4})'

# 调换模式group中对象的顺序
formatted_text = re.sub(pattern, r'\3-\1-\2', text)

print(formatted_text)
