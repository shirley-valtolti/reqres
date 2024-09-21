import requests

url = "https://reqres.in/api/users/2"

payload = 'name=morpheus&job=zion%20resident'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
