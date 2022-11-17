from data import ar,nev
from os import system
filename = 'termekek.csv'

def menu():
    system('cls')
    print('0 - Kilép')
    print('1 - Áruk listázása')
    print('2 - Aruk listázása árral')
    print('3 - Árucikk hozzáadása')
    return input('Választás: ')


def loadFromFile():
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        splitted = row.strip().split(';')
        nev.append(splitted[0])
        ar.append(float(splitted[1]))
    file.close() 

def showAruk():
    system('cls')
    print('Áruk')
    for name in nev:
        print(f'\t{name}')
    input()

def showArukAr():
    system('cls')
    print('Árucikkek árral')
    for arak,nevek in zip(nev,ar):
        print(f'{arak} - {nevek}Ft')
    input()

def addArucikk():
    system('cls')
    print('Új árucikk hozzáadása')
    name = input('Név: ')
    ara = float(input('Ára: '))
    nev.append(name)
    ar.append=(ara)
    saveResultToFile(name, ara)
    print('Sikeres felvétel.')
    input()

def saveResultToFile(name, ara):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{name};{ara}\n')
    file.close()