from data import *
from os import system
from math import *
filename = 'termekek.csv'

def menu():
    system('cls')
    print('0 - Kilép')
    print('1 - Áruk listázása árral')
    print('2 - Árucikk hozzáadása')
    print('3 - Bevásárlás')
    return input('Választás: ')


def loadFromFile():
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        splitted = row.strip().split(';')
        arnev[splitted[0]] = int(splitted[1])
    file.close() 
    

def showArukAr():
    system('cls')
    print('Árucikkek árral')
    for key, value in arnev.items():
        print(f'{key} - {value}')
    

def addArucikk():
    system('cls')
    print('Új árucikk hozzáadása')
    name = input('Név: ')
    ara = int(input('Ára: '))
    arnev[name] = ara
    saveResultToFile(name, ara)
    print('Sikeres felvétel.')
    

def saveResultToFile(name, ara):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{name};{ara}\n')
    file.close()


def bevasarlas():
    system('cls')
    showArukAr()
    input()
    penz = int(input('Pénzed:'))
    termek1 = input('Megvásárolni kívánt termék: ')
    i = searchTermek(termek1)
    termekAr = arnev[i]
    marad = penz - termekAr
    print(f'Ennyi pénzed maradt: {marad}Ft')
    input()

        
def searchTermek(needle):
    for name, point in arnev.items():
        if needle.upper() == name.upper():
            return name
    return False
