def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

if __name__ == "__main__":
    input_sentence = "Hello, World! Welcome to Python programming."
    expected = "programming. Python to Welcome World! Hello,"
    assert reverse_words(input_sentence) == expected