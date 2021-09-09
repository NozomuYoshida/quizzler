import requests

category_dict = {
    'General': 9,
    'Cs': 18,
    'History': 23,
    'Music': 12
}

URL = 'https://opentdb.com/api.php'
parameters = {
    'amount': 10,
    'type': 'boolean',
}

question_data_dict = {}
for category, category_number in category_dict.items():
    parameters['category'] = category_number
    response = requests.get(url=URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data['results']
    question_data_dict[category] = question_data



