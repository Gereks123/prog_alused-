ainepunktid = int(input('Sisestage ainepunktide arv: '))
ainepunktide_ajakulu = ainepunktid * 26
nädalate_arv = int(input('Sisestage nädalate arv: '))
nädala_ajakulu = round(float(ainepunktide_ajakulu / nädalate_arv))
print(nädala_ajakulu)