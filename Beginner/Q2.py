def count_digits_letters(input_string):
    digits = sum(1 for char in input_string if char.isdigit())
    letters = sum(1 for char in input_string if char.isalpha())
    return f"Alphabets: {letters} & Number: {digits}"


if __name__ == "__main__":
    assert count_digits_letters("Hello123") == "Alphabets: 5 & Number: 3"
    assert count_digits_letters("Hello") == "Alphabets: 5 & Number: 0"
    assert count_digits_letters("123") == "Alphabets: 0 & Number: 3"