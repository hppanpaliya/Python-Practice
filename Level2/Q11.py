def string_to_char_list(string_list):
    return list(map(list, string_list))

if __name__ == "__main__":
    input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
    expected = [
        ['R', 'e', 'd'],
        ['B', 'l', 'u', 'e'],
        ['B', 'l', 'a', 'c', 'k'],
        ['W', 'h', 'i', 't', 'e'],
        ['P', 'i', 'n', 'k']
    ]
    assert string_to_char_list(input_list) == expected