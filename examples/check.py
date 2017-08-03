import json
import requests
import time

from janitor import validation

# rv = requests.get('http://localhost:5000/api/issues/1')
# validation.check_issue(json.loads(rv.content))
# rv = requests.get('http://localhost:5000/api/issues/1099')
# validation.check_issue(json.loads(rv.content))
# rv = requests.get('http://localhost:5000/api/issues/1100')
# validation.check_issue(json.loads(rv.content))
# rv = requests.get('http://localhost:5000/api/issues/1101')
# validation.check_issue(json.loads(rv.content))

for issue_number in range(8505, 8490, -1):
    url = 'https://api.github.com/repos/webcompat/web-bugs/issues/{i}'.format(
        i=issue_number)
    rv = requests.get(url)
    validation.check_issue(json.loads(rv.content))
    time.sleep(2)
