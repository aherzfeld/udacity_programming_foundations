import os
# probably needs to be run with python3 because of input()
from shutil import copyfile

def map_names():
    # 2 - create dict {alpha: city}
    file_list = sorted(os.listdir('alphabet'))
    char_map = {}
    alpha_ord = ord('a')
    for file_name in file_list:
        if not file_name.startswith('.'):
            if alpha_ord <= 122:
                char_map[chr(alpha_ord)] = file_name
            elif alpha_ord == 123:
                char_map['.'] = file_name
            else:
                char_map[' '] = file_name
            alpha_ord += 1
    return char_map


def secret_message():
    # 1 accept user input message (alpha, . only)
    message = input('Secret message: ')
    file_list = sorted(os.listdir('alphabet'))
    char_map = {}
    alpha_ord = ord('a')
    for file_name in file_list:
        if not file_name.startswith('.'):
            if alpha_ord <= 122:
                char_map[chr(alpha_ord)] = file_name
            elif alpha_ord == 123:
                char_map['.'] = file_name
            else:
                char_map[' '] = file_name
            print(chr(alpha_ord), alpha_ord)  # testing
            alpha_ord += 1
    print(char_map)
    saved_path = os.getcwd()
    os.chdir('alphabet')
    # create dict with count of each char
    d = dict.fromkeys(message, 0)
    n = 0
    for c in message:
        d[c] += 1
        if d[c] >= 1:
            copyfile(char_map[c], str(n) + char_map[c])
            print(char_map[c], c)  # for testing
            n += 1
    os.chdir(saved_path)
    print('view files to see your message')


secret_message()
