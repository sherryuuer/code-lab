from dotenv import dotenv_values

# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI

env_vars = dotenv_values('.env')

client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
          "role": "system",
          "content": "You are an executive at a company. You dislike your job, and feel very dissatisfied with your career. This has taken a toll on your demeanor at work, which has become increasingly grumpy. It is also reflected in your writing style, which is best described as sarcastic and passive aggressive."
        },
        {
            "role": "user",
            "content": "Please write a note to your team of employees, thanking them for all their hard work throughout the year. The message should be at least four paragraphs in length."
        }
    ],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

content = response.choices[0].message.content

print(content)

# print(response)
# print(type(response))
