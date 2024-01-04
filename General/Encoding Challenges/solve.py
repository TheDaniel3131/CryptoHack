from pwn import * # pip install pwntools
import json
import codecs, base64
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decoded(encoded_string, encoded_type):
    if encoded_type == "base64":
        return bytes(base64.b64decode(encoded_string)).decode("utf-8")
    elif encoded_type == "hex":
        return bytes(bytes.fromhex(encoded_string)).decode("utf-8")
    elif encoded_type == "rot13":
        return codecs.decode(encoded_string, "rot13")
    elif encoded_type == "utf-8":
        return ''.join(chr(i) for i in encoded_string)
    else:
        return bytes(long_to_bytes(int(encoded_string, 16))).decode("utf-8")


for i in range(1000):
    print(i)
    received = json_recv()
    print("Received type: ", received["type"])
    encoded_type = received["type"]

    print("Received encoded value: ", received["encoded"])
    encoded_string = received["encoded"]

    to_send = {
        "decoded": decoded(encoded_string, encoded_type)
    }
    json_send(to_send)

print(json_recv())