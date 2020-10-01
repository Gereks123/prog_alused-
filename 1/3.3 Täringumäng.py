import random

taringud = int(input("Mitu täringut teil on vaja: "))

muutuja = 1
while(muutuja <= taringud):
    print(random.randint(1, 6))
    muutuja += 1