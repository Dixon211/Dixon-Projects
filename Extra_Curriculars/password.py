import pywifi
import time

auth_map = {
    pywifi.const.AUTH_ALG_OPEN: "Open",
    pywifi.const.AUTH_ALG_SHARED: "Shared Key"
}

wifi = pywifi.PyWiFi()
netcard = wifi.interfaces()[0]

netcard.scan()
time.sleep(2)
SSIDs = netcard.scan_results()
print("List of available SSIDs:")
for result in SSIDs:
    auth_method = [auth_map.get(result.auth, "unknown") for auth in result.auth]
    print(result.ssid + " " + auth_method)

#profile = pywifi.Profile()
