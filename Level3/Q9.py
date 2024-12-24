def run_length_encode(input_string):
    if not input_string:
        return ""
        
    result = []
    count = 1
    current_char = input_string[0]
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
            
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    input_str = "wwwwaaadebbbbbw"
    assert run_length_encode(input_str) == "w4a3d1e1b5w1"