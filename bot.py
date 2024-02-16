import pickle
from classes import *


class Bot:
    def __init__(self):
        # FILE_NAME = 'phone_book.pickle'
        self.file = 'phone_book.pickle'
        self.book = AddressBook()
        try:
            with open(self.file, 'rb') as fh:
                read_book = pickle.load(fh)
                self.book.data = read_book
        except:
            print('New phone book has been created\n')
   

    def run(self):


        commands = {




            # New contact, phone, birthday - - - > 1 Alex 1111111111 31.12.1700
            "1": add_contact_phone_birthday,
            "2": add_contact,                # New contact                  - - - > 2 Alex
            "3": add_phone,                  # Add phone                    - - - > 3 Alex 2222222222
            # Add birthday                 - - - > 4 Alex 31.12.1700
            "4": add_birthday,
            "5": edit_name,                  # Edit name                    - - - > 5 Alex Alexandr
            # # Edit phone                   - - - > 6 Alexandr 2222222222 3333333333
            "6": edit_phone,
            # # Edit birthday                - - - > 7 Alexandr 31.12.1701
            '7': edit_birthday,
            "8": days_to_birthday,           # Day to birthday              - - - > 8 Alexandr
            "search": search,                     # Search                       - - - > 9 text
            "remove": remove,
            "show all": show_all,                  # Show all contact            - - - > show all
            'help': help,                      # Commands list               - - - > help
            # # Good bye!                   - - - > good bye / exit / close
            'good bye': good_bye,

        }


        while True:
            try:
                user_input = console_input()
                function, *data = parser(user_input, commands)
                result = function(book, data)

                if result is not None:
                    print(result)
                if result == 'Good bye!':
                    break

            except:
                print('\n Check your input! \n')
