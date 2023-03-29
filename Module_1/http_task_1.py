import requests

heroes = []
url = 'https://akabab.github.io/superhero-api/api/all.json'
headers = {'Content-Type': 'application/json'}
result = requests.get(url=url)

[heroes.append([person['powerstats']['intelligence'], person['name']])\
 for person in result.json() if person['name'] in ['Hulk', 'Captain America', 'Thanos']]
print(f'Самый умный: {max(heroes)[1]}')
