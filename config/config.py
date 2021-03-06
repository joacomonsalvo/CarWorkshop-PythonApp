import json
import os

USERNAME = os.getlogin()
PATH = 'C:/Users/{}/Documents/Projects/Vehicles/config/'.format(USERNAME)

data_list = []


def start():
    "Start messages"
    print("Let's start configuring the app: ")
    print('Before that you need to accept the terms and conditions of the app\r\n')


def choose_idiom():
    'Select App Language'
    print('Select your language: ')
    print('1) Spanish')
    print('2) English\r\n')  
    option = int(input('Type the number of the option you want to chose:\r\n'))

    if option == 1:
        idiom = 'Spanish'
        data_list.append(idiom)
    elif option == 2:
        idiom = 'English'
        data_list.append(idiom)
    else:
        print("That's not an option, try again\r\n")
        choose_idiom()


def country_plate():
    "Select Country"
    print('Select your country for the plate design: ')
    print('1) Argentina')
    print('2) United States\r\n') 
    plate = int(input('Type the number of the option you want to chose:\r\n'))

    if plate == 1:
        country = 'Argentina'
        data_list.append(country)
    elif plate == 2:
        country = 'United States'
        data_list.append(country)
    else:
        print("That's not an option, try again")
        country_plate()


def write_in():
    "Write data in .json"
    dict0 = {
        'language': data_list[0],
        'country': data_list[1]
    }

    with open(PATH + 'data_file.json', 'w') as outfile:
        json.dump(dict0, outfile, indent=2)


def config():
    "CONFIG APP"
    start()
    choose_idiom()
    country_plate()
    write_in()


config()
