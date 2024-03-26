import requests

url = "http://127.0.0.1:5000/newdata"

data = [{"DefaultGateway":"30.30.30.30","LocalAddress":"30.30.30.30","MACAddress":"0000-0000-0002","MachineName":"TestName3"}]

response = requests.get(url, json=data)

if response.status_code == 200:
    print(f"Connection Successful!\nResponse: {response.text}")
else:
    print(f"something went wrong: {response.status_code}")