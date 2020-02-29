import os
import pickle
import json
import asyncio
import requests


# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

### FUNCTIONS ###

products: []

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  Greeter - Hello python crawler!  ***")
    print("\t**********************************************")
    
def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of agencies.")
    print("[2] Get products from other site.")
    print("[3] Start crawling data from agences.")
    print("[q] Quit.")
    
    return input("What would you like to do? ")
    
def show_agencies():
    # Shows the names of everyone who is already in the list.
    print("\nHere are the agencies I know.\n")

    f = open("input.json")
    jsonInput = json.load(f)
    for name in jsonInput['ota']:
        print('>', name)
        
def get_products():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.status_code)
    print(response.json())


    # f = open("input.json")
    # jsonInput = json.load(f)
    # for product in jsonInput['list']:
    #     print('>', product['agence'])
        
def start_crawler():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        crawler = __import__('crawler')
        crawler.start()
    except Exception as e:
        print(e)
        return []
        
def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these names.")
        print(e)
        
### MAIN PROGRAM ###
choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        show_agencies()
    elif choice == '2':
        get_products()
    elif choice == '3':
        start_crawler()
    elif choice == 'q':
        quit()
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")