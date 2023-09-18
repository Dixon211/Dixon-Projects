import pywifi
from pywifi import const

class SSID:
    def __init__(self, info):
        self.info = info
        self.security = self.info.akm[0]
        self.cipher = self.info.cipher
        self.name = self.info.ssid

    def get_cipher(self):
        cipher_mapping = {
            pywifi.const.CIPHER_TYPE_NONE: 'NONE',
            pywifi.const.CIPHER_TYPE_WEP: 'WEP',
            pywifi.const.CIPHER_TYPE_TKIP: 'TKIP',
            pywifi.const.CIPHER_TYPE_CCMP: 'AES',
            pywifi.const.CIPHER_TYPE_UNKNOWN: 'UNKNOWN'
        }

        cipher_str = cipher_mapping.get(self.cipher, "Unknown")
        return(cipher_str)

    def __str__(self):
        return f"SSID: {self.name}, Security: {self.cipher}"




wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Use the first network interface

iface.scan()  # Initiate a scan for nearby SSIDs

scan_results = iface.scan_results()

available_connections = []
for result in scan_results:
    ssid_instance = SSID(result)
    available_connections.append(ssid_instance)

for connection in available_connections:
    print(connection)



#for result in scan_results:
   # print("SSID:", result.ssid)
   # print("Signal Strength:", result.signal)