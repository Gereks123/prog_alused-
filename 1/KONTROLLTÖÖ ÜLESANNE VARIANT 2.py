import random

def konemaksumus(kone_maksumus):
    return kone_maksumus

#Siin on inputid
koneminuti_hind = float(input("Sisestage oma kõneminuti hind:"))

konede_koguarv = int(input("Sisestage oma kõnede arv:"))

suvaline_arv = random.choice(konekestus)

kone_maksumus = suvaline_arv / koneminuti_hind

min_hind = 60

max_hind = 600


konekestus = []

for i in range (10):
    n = random.randint(1, 1001)
    konekestus.append(n)
    print(konekestus)


