import os



def get_even_length_strings(filename):
    even_strings = []
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if len(word) % 2 == 0:
                    even_strings.append(word)
    return even_strings

if __name__ == '__main__':
    # create file
    with open('doc.txt', 'w') as f:
        f.write('Hello I am a file\n')
    
    result = get_even_length_strings('doc.txt')
    assert result == ['am', 'file']

    # clean up
    os.remove('doc.txt')


