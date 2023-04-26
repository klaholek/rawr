
# lista = []

# print("Podaj liczbę:")
# cyfra = int(input())

# for i in range(0, cyfra):
#     lista.append(i)
    

# slownik = {"Polska":"Warszawa","Rosja":"Moskwa","Hiszpania":"Madryt","Francja":"Paryż"}

# print("Podaj nazwę kraju")
# kraj = input()

# if kraj in slownik:
#     print("Stolicą tego kraju jest:", slownik[kraj])
# else:
#     print("Brak danych")


import random
import time

# num1 = ()
# num2 = ()
# wynik = ()
# lista = []
# poprawne = 0

# for i in range(3):
#     print("Wykonaj działanie na czas:")
#     num1 = random.randint(1,1000)
#     num2 = random.randint(1,100)
#     print(num1, "-", num2,)
#     print("Podaj wynik:")
#     start = time.time()
#     odp = int(input())
#     wynik = num1 - num2
    
#     if odp == wynik:
#         stop = time.time()
#         poprawne+=1
#         rt1 = stop - start
#         rt2 = round(rt1,2)
#         lista.append(rt2)
#     else:
#         continue
    

# print("Tyle masz poprawnych odpowiedzi:", poprawne)
# print(lista)




wpis1 = ["Kanapka","10:10","Z tofu - bardzo dobra"]
wpis2 = ["Fasoleczka","14:30","Mogła być lepsza, ale to Patrycja robiła"]
fl = [wpis1, wpis2]
wpis = []

print("Twój Food log")
print("Wciśnij podaną cyfrę, aby wybrać opcje")
print("1 Dodaj posiłek")
print("2 Usuń posiłek")
print("3 Wyświetl konkretny posiłek")
print("4 Wyświetl wszystkie posiłki")
print("5 Wyjście")

while True:
    odp1 = input()
    


    if odp1 == "1":
        print("Wpisz posiłek:")
        pos = input()
        wpis.append(pos)
        print("Wpisz o której:")
        czas = input()
        wpis.append(czas)
        print("Notatka:")
        note = input()
        wpis.append(note)

        fl.append(wpis)

    elif odp1 == "2":
        for i in range(len(fl)):
            print(fl[i])
        print("Który podaj nazwę posiłku, aby usunąć wpis:")
        odp2 = input()

        if odp2 == wpis[0]:
            wpis.remove(wpis)

print(fl)