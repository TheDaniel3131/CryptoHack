def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return [byte for row in matrix for byte in row]


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(bytes2matrix(matrix))
print(matrix2bytes(matrix))

# To obtain the resulting plaintext, you can convert the matrix to bytes to plaintext format
result = ''.join(map(chr, matrix2bytes(matrix)))
print(result)