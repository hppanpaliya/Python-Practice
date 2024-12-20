def get_unique_elements(list1):
    return list(dict.fromkeys(list1))

if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 4, 4, 5, 5]
    assert get_unique_elements(list1) == [1, 2, 3, 4, 5]