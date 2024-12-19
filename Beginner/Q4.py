def sum_odd_numbers(start, stop):
    return sum(num for num in range(start, stop + 1) if num % 2 != 0)


if __name__ == '__main__':
    assert sum_odd_numbers(1, 10) == 25
    assert sum_odd_numbers(1, 5) == 9