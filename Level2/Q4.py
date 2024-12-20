def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    D = 2
    assert rotate_array(arr, D) == [4, 5, 1, 2, 3]