from math import factorial
n = 2048
for i in range(n):
	probability = 1 - factorial(n) / (factorial(n - i)*pow(n,i))
	if probability > 0.75:
		print(i)
		breakn = 1 << 11
P = 1
for i in range(1, n):
    P = pow((1 - 1/n), i)
    nP = 1 - P
    if nP > 0.5:
        print(i)
        break