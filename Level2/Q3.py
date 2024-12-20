def count_pairs_with_sum(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1
    return count

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 6
    assert count_pairs_with_sum(arr, k) == 2

