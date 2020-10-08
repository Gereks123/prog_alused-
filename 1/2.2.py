perekonnanimi = input("Sisestage perekonnanimi: ")

if perekonnanimi[-2:] == "ne":
    print("Abielus")
elif perekonnanimi[-2:] == "te":
    print("Vallaline")
elif perekonnanimi[-1] == "e":
    print("Määramata")
elif perekonnanimi[-1] != "e":
    print("Tõenäoliselt ei ole leedulanna")