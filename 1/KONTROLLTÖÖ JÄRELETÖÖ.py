from random import *



def kilomeetrid(sammud_paevas, sammu_pikkus_meetrites):
    kilomeetrite_arv = (sammud_paevas * sammu_pikkus_meetrites) / 1000

    sammud_meet = int(input("Sisestage sammu pikkus meetrites: "))

    sammud = []

    for i in range(7):
        n = randint(4999, 15001)
        sammud.append(n)
        print(sammud)


    ip = 0
    while ip < 7:
        print(sammud[ip]/1000)
        ip += 1


    #Siin on iga päeva summa kilomeetrites
    kogu_km_summa = ((sum(sammud)) * sammud_meet / 1000)

    print("Igapäevaga kokku kilomeetreid oli: " + str(round(kogu_km_summa)))

    #Siin on keskmine arvutmaine


    avg = sum(sammud) / len(sammud)
    print("Keskmine on: " + str(round(avg,2)))

    if avg >= 10000:
        print("Tubli, läbitud arvude summa on piisav")
    else:
        print("Järgmisel nädalal tuleb entusiastlikumalt kõndida!")

    return (kilomeetrite_arv)
kilomeetrid(1, 2)