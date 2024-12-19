def single_digit_sum(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num


if __name__ == '__main__':
    assert single_digit_sum(987) == 6