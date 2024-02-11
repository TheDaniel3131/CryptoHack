ctext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

flag = ""
for value in range(256):
    flag = ''.join([chr(value ^ v) for v in bytes.fromhex(ctext)])
    if flag.startswith("crypto{"):
        print(flag);