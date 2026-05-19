import requests

url = input("Enter API URL: ")

data = {
    "username": "admin",
    "password": "admin"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.text)
