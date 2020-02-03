import requests

request = requests.get('http://api.open-notify.org')
print(request.text)

print(request.status_code)
200

request2 = requests.get('http://api.open-notify.org/fake-endpoint')
print(request2.status_code)
404

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)