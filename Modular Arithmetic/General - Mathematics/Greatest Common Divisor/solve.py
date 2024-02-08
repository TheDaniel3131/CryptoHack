def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 66528
b = 52920
print("gcd({}, {}) = {}".format(a, b, gcd(a, b)))
