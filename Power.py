# This function returns the power of a given number
def power(base, exponent):
    result = 1
    for index in range(exponent):
        result *= base
    return result