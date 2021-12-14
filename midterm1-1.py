# Author: CMOB 12/14/2021

from random import randint

def name_generator():
    computer = 0
    name_lst = []
    x = 0
    while True:
        computer = randint(0, 9999)
        new_name = str.capitalize(input("Would you like a new name?"))
        if new_name == "Y":
            if computer < 10:
                name = "CT-000" + str(computer)
                print("New clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif computer < 100 and computer >= 10:
                name = "CT-00" + str(computer)
                print("New clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif computer < 1000 and computer >= 100:
                name = "CT-0" + str(computer)
                print("New clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif computer >= 1000:
                name = "CT-" + str(computer)
                print("New clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

        if new_name == "N":
            print(name_lst)
            break

name_generator()
