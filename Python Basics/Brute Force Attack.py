import requests

url = ""
username = ""

f = open("password.txt", "r")
file = f.readlines()

for password in file:
    password = password.strip()

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=data)

    try:
        result = response.json()
        print(result)

        if result.get("login") == True:
            print("login")
            print(password)
            break
        else:
            print("login failed")

    except ValueError:
        print("invalid json")

f.close()