def calculate_lcm(num1, num2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(num1 * num2) // gcd(num1, num2)


if __name__ == "__main__":
    assert calculate_lcm(12, 18) == 36