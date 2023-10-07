import socket
import pywifi

wifi = pywifi.PyWiFi()
networkc = wifi.interfaces()[0]

networkc.scan()
network_scan_results = networkc.scan_results()

results = {}
for result in network_scan_results:
    print(f"SSID: {result.ssid}\nAuth Type: {result.auth}\nEncryption: {result.akm}\n\n")
    results[result.ssid] = result

answer = input("What network do you want to connect to?\n")


for ssid, network in results:
    if answer == ssid:
        