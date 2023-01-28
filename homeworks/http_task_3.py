import datetime
import time
import requests
to_date = datetime.date.today()
from_date = to_date - datetime.timedelta(days=2)
to_date = int(time.mktime(to_date.timetuple()))
from_date = int(time.mktime(from_date.timetuple()))
site_url = 'https://api.stackexchange.com'
questions = []

for pages in range(1, 26):
    query_str = f'{site_url}/2.3/questions?page={pages}&pagesize=100&fromdate={from_date}&todate={to_date}&order=desc&sort=activity&tagged=Python&site=stackoverflow'
    result = requests.get(url=query_str)
    time.sleep(1)
    [questions.append(item['title']) for item in result.json()['items']]
    if result.json()['has_more'] == 'false':
        break

[print(question) for question in questions]
print(f'Total questions: {len(questions)}')