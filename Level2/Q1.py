def find_common_elements(l1, l2):
    return list(set(l1) & set(l2))

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    assert find_common_elements(l1, l2) == [4, 5]