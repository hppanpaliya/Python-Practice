def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid-1] + sorted_list[mid]) / 2
    return float(sorted_list[mid])


if __name__ == '__main__':
    number_list = [7, 2, 5, 1, 9, 3]
    assert find_median(number_list) == 4.0
