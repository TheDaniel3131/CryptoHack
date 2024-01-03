from Crypto.Util.number import *

message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

message_long = long_to_bytes(message)
print(message_long)

# Bytes to long revert lines
# message_long_to_bytes = bytes_to_long(message_long)
# print(message_long_to_bytes)

message_decoded_long_string = message_long.decode('utf-8')
print(message_decoded_long_string)
