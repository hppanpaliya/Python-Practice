def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


if __name__ == '__main__':
    assert reverse_number(12345) == 54321