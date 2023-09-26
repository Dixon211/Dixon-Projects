import subprocess

def gateway_ip():
    command = "ipconfig"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True, universal_newlines=True)
    ip_config = result.stdout.split(" ")
    ip_config = [element for element in ip_config if element != "." and element != "" and element !=":"]
    gatewayip = ip_config[ip_config.index("Gateway")+1]
    return gateway_ip
