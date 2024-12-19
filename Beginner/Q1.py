def check_number(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Consultadd - Python Training"
    elif num % 3 == 0:
        return "Consultadd"
    elif num % 5 == 0:
        return "Python Training"
    return str(num)


if __name__ == '__main__':
    assert check_number(3) == "Consultadd"
    assert check_number(5) == "Python Training"
    assert check_number(15) == "Consultadd - Python Training"
