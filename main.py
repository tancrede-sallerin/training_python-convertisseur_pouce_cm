pouce = 2.54
cm = 0.394

convertion = input("indiquer POUCE->CM si vous voulez convertir des pouces en cm, et CM->Pouce pour l'inverse: ")
valeur = float(input("rentrez la valeur à convertir: "))

try:
    if convertion == 'POUCE->CM':
        print(valeur*pouce, 'cm')
    elif convertion == 'CM->Pouce':
        print(valeur*cm, 'cm')
except:
    print("vous devez rentrer POUCE->CM ou CM->Pouce, puis un nombre")


