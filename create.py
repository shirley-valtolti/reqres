import requests

url = "https://reqres.in/api/users"

payload = 'name=morpheus&job=leader'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
