def is_primitive_element(g, p):
    # Check if g is a primitive element by testing powers of g
    current_power = 1
    while current_power < p - 1:
        if pow(g, current_power, p) == 1:
            return False
        current_power += 1
        return True

def find_primitive_element(p):
    # Iterate through possible values of g to find the smallest primitive element
    for g in range(2, p):
        if is_primitive_element(g, p):
            return g

p = 28151
primitive_element = find_primitive_element(p)
print("The smallest primitive element of Fp =", primitive_element)
