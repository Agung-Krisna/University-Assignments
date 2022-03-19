#!/usr/bin/env python3
#Convert temperatures into Celcius, Fahrenheit, Reamur, and Kelvin
from termcolor import colored


class temperatures:
    def __init__(self, heat):
        self.heat = heat

    def celcius(self):
        celcius = self.heat
        fahrenheit = ((celcius / 5) * 9) + 32
        kelvin = celcius + 273.15
        reamur = (celcius / 5) * 4
        return fahrenheit, kelvin, reamur

    def fahrenheit(self):
        fahrenheit = self.heat
        celcius = ((fahrenheit - 32) * 5) / 9
        reamur = ((fahrenheit - 32) * 4) / 9
        kelvin = (((fahrenheit - 32) * 5) / 9) + 273
        return celcius, reamur, kelvin

    def kelvin(self):
        kelvin = self.heat
        celcius = kelvin - 273.15
        reamur = ((kelvin - 273) * 5) / 9
        fahrenheit = (((kelvin - 273) * 9) / 5) - 32
        return celcius, reamur, fahrenheit
    
    def reamur(self):
        reamur = self.heat
        celcius = (reamur * 5) / 4
        kelvin = celcius + 273
        fahrenheit = ((reamur * 9) / 4) + 32
        return celcius, kelvin, fahrenheit

print("Welcome to", colored("magic converter", 'blue'), colored('for', 'green'), colored('temperatures', 'blue'))

print("What celcius do you have?")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Reamur")
print("4. Kelvin")

while True:
    try:
        choice = int(input())
        break
    except ValueError:
        continue


if choice == 1:
    while True:
        try:
            heat = int(input("enter heat\n"))
            break
        except ValueError:
            continue
    temps = temperatures(heat)
    (fahrenheit, kelvin, reamur) = temps.celcius()
    inner_choice = int(input("what do you want to convert into\n1. Fahrenheit\n2. Kelvin\n3. Reamur\n"))
    if inner_choice == 1:
        print(fahrenheit)
    elif inner_choice == 2:
        print(kelvin)
    elif inner_choice == 3:
        print(reamur)
    else:
        print('Are we there yet?')

if choice == 2:
    while True:
        try:
            heat = int(input("enter heat\n"))
            break
        except ValueError:
            continue
    temps = temperatures(heat)
    (celcius, reamur, kelvin) = temps.fahrenheit()
    inner_choice = int(input("what do you want to convert into\n1. Celcius\n2. Reamur\n3. Kelvin\n")) 
    if inner_choice == 1:
        print(celcius)
    elif inner_choice == 2:
        print(reamur)
    elif inner_choice == 3:
        print(kelvin)
    else:
        print('ZipZZip')

if choice == 3:
    while True:
        try:
            heat = int(input("enter heat\n"))
            break
        except ValueError:
            continue
    temps = temperatures(heat)
    (celcius, kelvin, fahrenheit) = temps.reamur()
    inner_choice = int(input("what do you want to convert into\n1. Celcius\n2. Kelvin\n3. Fahrenheit\n"))
    if inner_choice == 1:
        print(celcius)
    elif inner_choice == 2:
        print(kelvin)
    elif inner_choice == 3:
        print(fahrenheit)
    else:
        print('Not woohoo')
if choice == 4:
    while True:
        try:
            heat = int(input("enter heat\n"))
            break
        except ValueError:
            continue
    temps = temperatures(heat)
    (celcius, reamur, fahrenheit) = temps.kelvin()
    inner_choice = int(input("what do you want to convert into\n1. Celcius \n2. Reamur\n3. Fahrenheit\n"))
    if inner_choice == 1:
        print(celcius)
    elif inner_choice == 2:
        print(reamur)
    elif inner_choice == 3:
        print(fahrenheit)
    else:
        print('ZerroKarraHajjimaruyo')

if choice > 4:
    print('Try again, with no erroneous inputs, please')
