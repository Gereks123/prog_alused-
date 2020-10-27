fail = open("rebased.txt", encoding="UTF-8")
V_voetud = []
for rida in fail:
    V_voetud.append(int(rida))
for el in V_voetud:
    print(el)
L = input("Palun sisestage, millise aasta andmeid vajate(2011-2019): ")
jeet = int(L) - 2010
jeef = print(str(L) + ". aastal oli vastuvõetud " + str(V_voetud[int(L[3])-1]))
fail.close()