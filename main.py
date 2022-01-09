import requests
import fake_useragent

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}

link = 'https://www.instagram.com/'


def get_info(usernames):
    responce = requests.get(f'{link}{name}/')
    if responce.status_code == 200:
        return False


try:
    with open('usernames.txt') as file:
        names = file.readlines()
        print('[USER] Open files with usernames')
except FileNotFoundError:
    with open('usernames.txt', 'w') as file:
        file.write('#Please, write usernames')
    print('[USER] File not found')
    print('[USER] Input usernames with \', \'')
    names = str(input()).split(', ')

if names[0] == '#Please, write usernames' and len(names) == 1:
    print(names[0])
else:
    names.pop(0)
    for name in names:
        name = name.replace('\n', '')
        if get_info(name) == False:
            print(f'[USER] {name} - Занят')
        else:
            print(f'[USER] {name} - Свободен')
