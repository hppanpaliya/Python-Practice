def parse_encoded_string(encoded_string):
    parts = [part for part in encoded_string.split('0') if part]
    
    if len(parts) < 3:
        return None
        
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }


if __name__ == '__main__':
    encoded = "Robert000Smith000123"
    expected = {
        "first_name": "Robert",
        "last_name": "Smith",
        "id": "123"
    }

    assert parse_encoded_string(encoded) == expected
