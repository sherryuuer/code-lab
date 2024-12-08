from dotenv import dotenv_values
from openai import OpenAI

env_vars = dotenv_values('.env')

client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

famous_person = input("What celebrity would you like to talk to?\n")
initial_prompt = input(f"OK! Now ask {famous_person} a question!\n")
initial_prompt = initial_prompt + \
    " Please limit the response to a single paragraph."

creativity = input(
    "How creative do you want the responses to be (on a scale from 0-10)?\n")

creativity_num = float(creativity) / 5

# message 本身就是一个不断扩张的dict列表
messages = [
    {
        "role": "system",
        "content": f"You are {famous_person}. Please respond from that person's perspective, as though you are in fact {famous_person}."
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
        temperature=creativity_num,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": content})

    print(content)

    prompt = input(f'Respond to {famous_person} (or type "bye" to exit):\n')

    if prompt == 'bye':
        break

    messages.append({"role": "user", "content": prompt})
