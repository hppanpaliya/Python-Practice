def starts_with_char(input_string, given_char):
    check = lambda s, c: s.startswith(c)
    return check(input_string, given_char)

if __name__ == '__main__':
    input_string = "Hello, World!"
    given_char = "H"
    assert (starts_with_char(input_string, given_char) == True)
    assert (starts_with_char(input_string, "h") == False)