from fibonacci_sequence.fibonacci_sequence import *


commands = [
    'Create Sequence 10',
    'Locate 13',
    'Create Sequence 3',
    'Locate 10',
]

for command in commands:
    if 'Create' in command:
        print(*create_sequence(int(command.split()[-1])))
    else:
        print(locate(int(command.split()[-1])))


