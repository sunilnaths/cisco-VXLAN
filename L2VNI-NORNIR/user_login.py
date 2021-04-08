import yaml
import getpass


def user_login():
    user_list = dict()
    username = input("Enter username : ")
    password = getpass.getpass(prompt="Enter your Password : ")

    user_list = {'username': username, 'password': password}

    with open(r'defaults.yaml', 'w') as login:
        log = yaml.dump(user_list, login)
