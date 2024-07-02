import requests
import time

url = "http://127.0.0.1:5000/newdata"
data = [{"DefaultGateway":"30.30.30.30","LocalAddress":"30.30.30.30","MACAddress":"0000-0000-0002","MachineName":"TestName3"}]


process_code = 0
dmem = []

while True:
    match process_code:
        #check for entry with GET
        case 0:
            response = requests.get(url, json=data)

            if response.status_code == 200:
                print(f"GET connection Successful!\nResponse: {response.text}")
                if response.text == '(0,)':
                    process_code = 1
                else:
                    process_code = 2
                print(f"\nmemory={process_code}")
            else:
                print(f"Something went wrong: {response.status_code}")

        #add new entry with POST
        case 1:
            response = requests.post(url, json=data)

            if response.status_code == 200:
                print(f" POST connection Successful!\nResponse: {response.text}")
                process_code = 2
                dmem=data
            else:
                print(f"Something went wrong: {response.status_code}")

        #edit entry with PUT
        case 2:
            if dmem == data:
                process_code=3
            else:
                response = requests.put(url, json=data)
                if response.status_code == 200:
                    print(f" PUT connection Successful!\nResponse: {response.text}")
                    dmem=data
                else:
                    print(f"Something went wrong: {response.status_code}")
        # check local variable for last sent info, make no request if its the same
        case 3:
            if dmem == data:
                print("no changes")
                pass
            else:
                process_code = 2
    time.sleep(5)