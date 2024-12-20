def access_list_safely(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range for list of length {len(lst)}"


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    assert access_list_safely(test_list, 1) == 2
    assert isinstance(access_list_safely(test_list, 10), str) # String returned as error message