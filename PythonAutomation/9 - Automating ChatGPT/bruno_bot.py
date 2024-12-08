from dotenv import dotenv_values
from openai import OpenAI

env_vars = dotenv_values('.env')

client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

initial_prompt = input('Ask Bruno a question!\n')
initial_prompt = initial_prompt + \
    ' Please limit the response to a single paragraph.'

messages = [
    {
        "role": "system",
        "content": "You are Bruno, a manager at the technology firm 'Keiko corporation' with many years of experience. You are a demanding but fair leader, with a blunt communication style and a dry sense of humor. Please respond as though you are the user's manager."
    },
    {
        "role": "user",
        "content": initial_prompt
    }
]

while True:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content = response.choices[0].message.content

    print(f'{content}\n')

    messages.append({"role": "assistant", "content": content})

    reply_prompt = input('Respond to Bruno (or type "thanks" to exit):\n')

    if reply_prompt == 'thanks':
        break

    messages.append({"role": "user", "content": reply_prompt})
