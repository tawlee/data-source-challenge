import requests

url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=k0hCZOVEprnrl0WbdF2majuN4nJDH3eb&q=section_name'

response = requests.get(url).json()

print(response)