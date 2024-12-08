import requests

url = 'https://icanhazdadjoke.com/search'

request_params = {"term": "spaghetti"}

response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params=request_params
                        )

data = response.json()

jokes = data['results']

for joke in jokes:
    joke_text = joke['joke']
    print(joke_text)
