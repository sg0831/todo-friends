import requests, json

url = 'http://localhost:8000/api/user/'

data = {
	'username': 'tester2',
	'password': 'wkwjsrj1',
}
params = {
	'username': 'jsk0831'
}

res = requests.get( url, params=params )

print("status code: {}".format( res.status_code ) )
#print("text: {}".format( res.text ) )
print("json: {}".format( res.json() ) )