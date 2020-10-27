fail = open("konto.txt", encoding="UTF-8")
numbrid = []
for rida in fail:
    numbrid.append(float(rida))
for el in numbrid:
    if el > 0:
        print(el)
fail.close()