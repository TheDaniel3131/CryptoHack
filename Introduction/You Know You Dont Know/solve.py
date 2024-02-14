from pwn import *

flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

flag_2bytes = bytes.fromhex(flag)
print(flag_2bytes)

# Allocate Secret Key
find_secret_key = xor(flag_2bytes, 'crypto{'.encode())
print(find_secret_key) # Output: myXORkey

# Find the FLAG
the_flag = xor(flag_2bytes, 'myXORkey'.encode())
print(the_flag)