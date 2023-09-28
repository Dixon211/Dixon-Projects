import struct

def calculate_checksum(data):
    #initialize the checksum to zero
    checksum = 0
    
    #group data into 2 bytes then add
    for i in range(0, len(data), 2):
        chunk = data[i:i + 2]
        if len(chunk) == 2:
            checksum += struct.unpack('!H', chunk)[0]
    
    # Handle the case where the data length is odd by adding the last byte
    if len(data) % 2:
        checksum += struct.unpack('B', data[-1:])[0] << 8
    
    # Add the carry and take the one's complement
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum += checksum >> 16
    checksum = ~checksum & 0xFFFF

    return checksum