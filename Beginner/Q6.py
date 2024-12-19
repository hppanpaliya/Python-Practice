def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


if __name__ == '__main__':
    assert is_perfect_number(5) == False
    assert is_perfect_number(6) == True
