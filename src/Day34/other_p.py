from Day17.Question import Question
from Day17.Quiz_Brain import Quiz
import tkinter as tk
question_bank = []
import requests
parameter = {
    "amount":"10",
    "categories":"17",
    "type":"boolean"
}
response = requests.get("https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
# print(response.json())
question = response.json()["results"][0]["question"]
answer = response.json()["results"][0]["correct_answer"]
print(question)
print(answer)


