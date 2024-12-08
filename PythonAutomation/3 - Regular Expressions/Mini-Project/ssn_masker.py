import re


def mask_ssns(text):
    regex = r'\d{3}-\d{2}-(\d{4})'  # 用括号括起来的地方就是group的地方

    clean_ssns = re.sub(regex, r'***-**-\1', text)

    return clean_ssns


sample_text = 'An example of a valid SSN is 321-54-9876. However, 321-54 is NOT a valid SSN.'

print(mask_ssns(sample_text))
