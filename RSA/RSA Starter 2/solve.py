# N = p * q

# p = 17, q = 23
# e = 65537
# base = 12

p = 17
q = 23
N = p * q
answer = pow(12, 65537, N)
print(answer)