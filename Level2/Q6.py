def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)


if __name__ == '__main__':
    power_of_two = 16
    not_power_of_two = 15
    assert is_power_of_two(power_of_two) == True
    assert is_power_of_two(not_power_of_two) == False