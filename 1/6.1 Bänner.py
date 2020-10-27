def eelarve(kylalised):
    sook = 10 * kylalised
    rent = 55
    kokku = sook + rent
    return kokku

print(eelarve(5))

#Kasutaja sisend

kylaliste_koguarv = int(input("Mitu inimest on kutsutud?:"))

kylaliste_kindelarv = int(input("Mitu inimest tuleb?:"))

#arvutused
maksimaalne_eelarve = eelarve(kylaliste_koguarv)
minimaalne_eelarve = eelarve(kylaliste_kindelarv)

print("Maksimaalne eelarve on " + str(eelarve(kylaliste_koguarv)) + "eurot")
print("Minimaalne eelarve on " + str(eelarve(kylaliste_kindelarv)) + " eurot")