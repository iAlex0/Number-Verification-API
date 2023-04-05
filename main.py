import requests
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv('.env')
api_key = os.getenv('API')


URL = 'https://api.apilayer.com/number_verification'


def get_headers():
    return {
        'apikey': api_key
    }


def get_countries():
    endpoint = '/countries'
    response = requests.get(URL + endpoint, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        for country_code in data.keys():
            country = data[country_code]
            print(f"\033[32mCountry code:\033[0m {country_code}")
            print(f"\033[32mCountry name:\033[0m {country['country_name']}")
            print(f"\033[32mDialling code:\033[0m {country['dialling_code']}")
            print('-' * 50)
    else:
        print("\n\033[33mError:\033[0m", response.status_code)


def validate_number(number):
    endpoint = f'/validate?number={number}'
    response = requests.get(URL + endpoint, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        if data['valid']:
            print(f"\n\033[32mCountry:\033[0m {data['country_name']}")
            print(f"\033[32mLocation:\033[0m {data['location']}")
            print(f"\033[32mCarrier:\033[0m {data['carrier']}")
            print(f"\033[32mLine type:\033[0m {data['line_type']}")
            print(f"\033[32mInternational format:\033[0m {data['international_format']}")
            print(f"\033[32mLocal format:\033[0m {data['local_format']}")
            print(f"\033[32mCountry prefix:\033[0m {data['country_prefix']}")
            print(f"\033[32mCountry code:\033[0m {data['country_code']}")
            print('-' * 50)
        else:
            print("\033[31m\nError: Please enter a valid phone number:\033[0m")
            print('\033[34m(Ex: 14158586273)\033[0m')
    else:
        print("\n\033[33mError:\033[0m", response.status_code)


def main():
    is_first_loop = True
    
    while True:
        if is_first_loop:
            print('\nWelcome to the phone number validator. (Press q exit))')
            is_first_loop = False

        print("\033[33m" + "\nHere are the available commands: " + "\033[0m")
        print("1. Print a list of countries + area codes")
        print("2. Validate a phone number")
        print("3. Exit")
        
        command = input("\033[32m" + "\nEnter a command: " + "\033[0m").strip()
        if command == '3':
            break
        elif command == '1':
            get_countries()
        elif command == '2':
            print('Enter phone number including the prefix for validation.')
            print('\033[34m(Ex: 14158586273).\033[0m')
            print('-' * 20)
            number = input("\033[33m" + "\nEnter a number: " + "\033[0m").lower().strip()
            number = number.replace(' ', '').replace('-', '')
            validate_number(number)
        else:
            print("\033[31m\nError: Please enter a valid command.\033[0m")

if __name__ == '__main__':
    main()