import requests

url = input("Enter URL: ")

response = requests.get(url)

for header in response.headers:
    print(header + ":", response.headers[header])
