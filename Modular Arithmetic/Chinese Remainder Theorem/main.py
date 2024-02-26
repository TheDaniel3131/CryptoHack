def invmod(a, m):
    # Function to calculate modular multiplicative inverse
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1

def ChineseRemainderGauss(n, N, a):
    # n is the list of moduli
    # N is the product of all moduli
    # a is the list of remainders
    # x is the solution
    x = 0
    for i in range(len(n)):
        ai = a[i]
        ni = N // n[i]
        x += ai * ni * invmod(ni, n[i])
    return x % N

# Gauss Algorithm

# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

n = [5, 11, 17]
N = 935
a = [2, 3, 5]

print(ChineseRemainderGauss(n, N, a))
