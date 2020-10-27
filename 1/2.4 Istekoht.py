from random import *
üks = input("Kas soovite istekohta ise valida (ise) või loosida (loos)? ")
if üks == "ise":
    kaks = input("Kas soovite istuda akna ääres (aken) või mitte (muu)? ")
    if kaks == "aken":
        print("valisite ise. Aknakoht")
    else:
        print("Valisite Ise. Vahekäigukoht")
else:
    i = randint(1,3)
    if i == 1 or 2:
        print("Istekoht loositi. Vahekäigukoht")
    else:
        print("Istekoht loositi. Aken")