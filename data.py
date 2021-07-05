import requests as rfq

parameters = {
     "amount": 10,
     "type": "boolean",
     "category": 18 # Category represents the class of questions downloaded from website

}
"""The questions for the quiz are used using the below API from opendb"""

response = rfq.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
