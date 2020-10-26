from database import Database
import os

def getAllMode():
    data = {}
    file_list = os.listdir('mode')
    for file in file_list:
        with open('mode/{}'.format(file), 'r', encoding='utf-8') as f:
            data[file] = f.read()
    return data

def choiseMode(mode_name):
    all_mode = getAllMode()
    for mode in all_mode:
        if mode_name == mode:
            return {'title': mode_name, 'content': all_mode[mode_name]}

if __name__ == '__main__':
    print(getAllMode())