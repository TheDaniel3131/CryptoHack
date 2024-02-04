state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    result = []
    for i in range(len(s)):
        row = [s[i][j] ^ k[i][j] for j in range(len(s[i]))]
        result.append(row)
    return result

def matrix2bytes(matrix):
    # Assuming each element in the matrix is a byte
    return bytes([element for row in matrix for element in row])

result_matrix = add_round_key(state, round_key)
flag_bytes = matrix2bytes(result_matrix)

# Now you can use the flag_bytes to get your next flag
print(flag_bytes)
