def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Given primes p and q
p = 26513
q = 32321

# Calculate gcd(p, q), and the coefficients u and v
gcd, u, v = extended_gcd(p, q)

# Ensure that u is the lower number
if u < v:
    print(u)
else:
    print(v)


# Enter whichever of u and v is the lower number as the flag.
# Answer: -8404

# crypto{10245, -8404}