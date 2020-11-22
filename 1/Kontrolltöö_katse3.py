from random import *

sammud = []

def Kilomeetrid(sammud, sammud_meeter):
    kilomeetrite_arv = (sammud * sammud_meeter) / 1000
    return(kilomeetrite_arv)

sammud_meeter = int(input("Sisestage sammude pikkus meetrites: "))

for i in range(7):                 #tsükkel, mis lisab suvalist 7 arvu vastavas vahemikus
    suvaline = randint(5000, 15000)
    sammud.append(suvaline)


print("Sammude arvud vastavas järjekorras: ")    #tsükliga väljastab igal päeval läbitud sammude arvud
ip = 0
while ip < 7:
    print(str(sammud[i]), "sammu")
    ip += 1

print("Sammud arvutatud kilomeetriteks: ")    #tsükliga väljastab meetrid kilomeetritena
i = 0
while i < 7:
    print(str(round((sammud[i] * sammud_meeter) / 1000)), "km")
    i += 1

Km_summa = (sum(sammud * sammud_meeter) / 1000)       #7 päeva läbitud kilomeetrite arv
print("Kilomeetreid iga päev kokku: " + str(round(Km_summa)) + " km")

def keskmine_arv(num):              #leiab 7 päeva keskmise sammude arvu
    summa = 0
    for t in num:
        summa = summa + t

    avg = summa / len(num)
    return avg

print("Keskmine sammude arv päevas: ", round(keskmine_arv(sammud)), "sammu") #kui sammud on üle 1000 siis on kõik korras, kui on alla 10000 siis peab rohkem pingutama

if keskmine_arv(sammud) > 10000:
    print("Keskmine sammude arv nädalas on 10000, olete heal järjel!")
else:
    print("Keskmine sammude arv nädalas on alla 10000, peate rohkem liikuma!!!!!")


Kilomeetrid (1000, 2)