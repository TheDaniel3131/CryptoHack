import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Need to stioll hex_string to bytes first for encode to Base64
hex_2_bytes = bytes.fromhex(hex_string)
print(hex_2_bytes)

# Encode the bytes to Base64
hex_2_bytes_string = base64.b64encode(hex_2_bytes)
print(hex_2_bytes_string)

# Then Decode the Base64.
print(hex_2_bytes_string.decode())