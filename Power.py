def power(base, exponent):
    result = 1
    for index in range(exponent):
        result *= base
    return result