import os

if os.path.exists('File Writer/my_first_file.txt'):
    os.remove('File Writer/my_first_file.txt')
else:
    print('File already deleted!')