import requests

url = "http://127.0.0.1:5000/newdata"
data = [{"DefaultGateway":"30.30.30.30","LocalAddress":"30.30.30.30","MACAddress":"0000-0000-0002","MachineName":"TestName3"}]

print("\nStarting Test\n\n")

def test(url, data):

    response = requests.get(url, json=data)
    if response.status_code == 200:
        print(f"GET Connection Successful!\nResponse: {response.text}\n\n")
    else:
        print(f"something went wrong: {response.status_code}\n\n")

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"POST Connection Successful!\nResponse: {response.text}\n\n")
    else:
        print(f"something went wrong: {response.status_code}\n\n")

    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"PUT Connection Successful!\nResponse: {response.text}\n\n")
    else:
        print(f"something went wrong: {response.status_code}\n\n")

    response = requests.delete(url, json=data)
    if response.status_code == 200:
        print(f"DELETE Connection Successful!\nResponse: {response.text}\n\n")
    else:
        print(f"something went wrong: {response.status_code}\n\n")

    return 0

test(url, data)

