# Q1
import sys
line_no = 1

try:
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            print(f'{line_no:5} {line}', end='')
            line_no += 1
except IndexError:
    print(f'{sys.argv[0]}: Missing required argument.')
except FileNotFoundError:
    print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')

# Q2
import sys

try:
    with open(sys.argv[1], 'r') as first, open(sys.argv[2], 'r') as second:
        if first.read() == second.read():
            print('Files are the same.')
        else:
            print('Files are different')
except IndexError:
    print(f'{sys.argv[0]}: Missing required argument(s).')
except FileNotFoundError:
    print(f'{sys.argv[0]}: Error opening files to compare.')

# Q3
import sys

try:
    file_name = sys.argv[2]
    pattern = sys.argv[1]

    with open(file_name, 'r') as infile:
        for line in infile:
            if pattern in line:
                print(line, end='')
except IndexError:
    print(f'{sys.argv[0]}: Missing required argument.')
except FileNotFoundError:
    print(f'{sys.argv[0]}: Cannot open "{sys.argv[2]}"')

# Q4
import sys

lines = words = characters = 0

try:
    with open(sys.argv[1], 'r') as infile:
        for line in infile.readlines():
            lines += 1
            words += len(line.split())
            characters += len(line)

    print(f'Lines:      {lines:6}')
    print(f'Words:      {words:6}')
    print(f'Characters: {characters:6}')

except IndexError:
    print(f'{sys.argv[0]}: Missing required argument.')
except FileNotFoundError:
    print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')

# Q5
import sys

LINUX_WORD_LIST = '/usr/share/dict/words'
MY_WORD_LIST = './words_alpha.txt'


def load_dictionary(word_file=MY_WORD_LIST):

    word_list = []

    with open(word_file, 'r') as words:
        for word in words.readlines():
            word_list.append(word[:-1])

    return word_list


def clean_word(dirty_word):
    from string import ascii_lowercase as letters

    return ''.join([c.lower() if c.lower() in letters else '' for c in dirty_word])


def is_word(possible_word):
    return possible_word.isalpha()

try:
    real_words = load_dictionary()
except FileNotFoundError:
    print(f'{sys.argv[0]}: Cannot open the dictionary file.')
else:
    try:
        with open(sys.argv[1]) as file_to_check:
            for line in file_to_check:
                for word in line.split():
                    if is_word(word) and clean_word(word) not in real_words:
                        print(word)

    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')