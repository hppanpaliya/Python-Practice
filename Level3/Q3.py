import os
def JtoI():
    with open('WORDS.TXT', 'r') as file:
        content = file.read()
    corrected_content = content.replace('J', 'I')
    print(corrected_content)

if __name__ == '__main__':
    # create file
    with open('WORDS.TXT', 'w') as f:
        f.write('THJS JS A NOTEBOOK')
    
    JtoI()
    
    # clean up
    os.remove('WORDS.TXT')