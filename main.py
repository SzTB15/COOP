from functions import *

loadFromFile()
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        showAruk()
        input()
    elif choice == '2':
        showArukAr()
        input()
    elif choice == '3':
        addArucikk()
    
