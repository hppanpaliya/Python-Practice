def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


if __name__ == '__main__':
    assert is_anagram("listen", "silent") == True