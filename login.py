import requests

url = "https://reqres.in/api/login"

payload = 'email=eve.holt%40reqres.in&password=cityslicka'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)