import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")

questions = response.json()

question_data = questions["results"]
