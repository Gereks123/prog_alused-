import random
import math
basseiniotsad = [] #Otsade array


def Kalorid(basseiniotste_arv, basseinipikkus): #Kalorite arvutamine

    kulunud_kalor = float((basseiniotste_arv * basseinipikkus / 1000) * 120)
    return (kulunud_kalor)

uks_ots = input("Mitu meetrit on üks basseini ots?: ")




for i in range(7): #Lisatakse 7 suvalist basseiniotsa arvu ja kuvatakse kui palju kulus igal päeval.
    arv = random.randint(25, 50)
    basseiniotsad.append(arv)
    kalorid = float(Kalorid(basseiniotsad[i], int(uks_ots)))
    print("Kaloreid kulus:", kalorid) #Arvutab kalorid


 #Ei saanud vastust kokku liita, proovisin igati













