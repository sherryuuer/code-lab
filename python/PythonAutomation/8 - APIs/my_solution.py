import requests
import html
import csv

while True:
    try:
        num = int(input("Enter the number of trivia questions you want: "))
        break
    except:
        print("Please enter a vaild number")

while True:
    difficulty = input(
        "Enter the difficulty of the questions (easy/medium/hard): ").lower()
    if difficulty in ["easy", "medium", "hard"]:
        break

endpoint = 'https://opentdb.com/api.php'
params = {
    "amount": num,
    "difficulty": difficulty,
    "category": 18
}

response = requests.get(endpoint,
                        headers={"Accept": "application/json"},
                        params=params,
                        )

data = response.json()
results = data["results"]

lst = [["Question", "Answer"],]
for dict in results:
    question = html.unescape(dict["question"])
    answer = html.unescape(dict["correct_answer"])
    if type(dict["type"]) == "boolean":
        question = question + " True or False?"
    lst.append([question, answer])


with open("result.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(lst)
