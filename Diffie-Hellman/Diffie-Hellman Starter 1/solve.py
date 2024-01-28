p = 991
g = 209

# find the inverse element, d
# formula: g * d mod 991 = 1

sol = pow(209, -1, 991)
print(sol)