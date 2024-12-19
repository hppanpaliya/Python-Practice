def count_frequency(input_list):
    frequency = {}
    for item in input_list:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


if __name__ == "__main__":
    input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
    assert count_frequency(input_list) == {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}