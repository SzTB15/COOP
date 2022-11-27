from functions import *

loadFromFile()
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        showArukAr()
        input()
    elif choice == '2':
        addArucikk()
    elif choice == '3':
        bevasarlas()