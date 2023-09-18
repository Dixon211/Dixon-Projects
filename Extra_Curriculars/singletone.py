import pywifi

# Create a PyWiFi object
wifi = pywifi.PyWiFi()

# Get the first network interface (you can choose a specific one if needed)
iface = wifi.interfaces()[0]

# Start scanning for nearby SSIDs
iface.scan()

# Get the scan results
scan_results = iface.scan_results()

# Iterate through the scan results
SSID = []
for result in scan_results:
    ssid = result.ssid
    SSID.append(ssid)
    
    # Connect to the network (you may need to provide a password or credentials here)
    iface.connect(ssid)
    
    # Retrieve the cipher information from the connected interface
    cipher_type = iface.status().cipher
    
    print(f"SSID: {ssid}, Cipher Type: {cipher_type}")
    
    # Disconnect from the network
    iface.disconnect()