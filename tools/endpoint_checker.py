import requests

domain = input("Enter domain: ")

endpoints = [
    "/api",
    "/api/login",
    "/api/users",
    "/admin",
    "/dashboard"
]

for endpoint in endpoints:
    url = domain + endpoint

    try:
        r = requests.get(url, timeout=3)
        print(url, ":", r.status_code)
    except:
        pass
