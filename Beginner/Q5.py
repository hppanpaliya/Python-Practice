def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1