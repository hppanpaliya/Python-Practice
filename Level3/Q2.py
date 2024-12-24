
import os
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

if __name__ == '__main__':
    # create file
    with open('demo.txt', 'w') as f:
        f.write('Line 1\nLine 2\nLine 3\n')
    
    result = count_lines('demo.txt')
    assert result == 3

    # clean up
    os.remove('demo.txt')