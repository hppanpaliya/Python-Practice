def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

if __name__ == '__main__':
    string = "Hello, World!"
    assert count_vowels(string) == 3