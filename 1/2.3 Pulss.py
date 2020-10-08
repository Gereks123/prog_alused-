vanus = int(input("Sisestage oma vanus: "))
sugu = input("Sisestage oma sugu(M/N): ").upper()
tuup = int(input("Valige tüüp numbrina: 1) tervisetreening 2)põhivastupidavuse treening 3)intensiivne aeroobne treening: "))
max_M_sagedus = 220 - vanus
max_N_sagedus = 206 - (vanus * 0.88)

def koormus():
    if sugu[0] == "M":
        if tuup == 1:
            koormus_1 = max_M_sagedus * 0.5
            koormus_2 = max_M_sagedus * 0.7
            print("Pulsisagedus peaks olema vahemikus " + str(int(koormus_1))) + " kuni " + str(int(koormus_2))
        if tuup == 2:
            koormus_1 = max_M_sagedus * 0.7
            koormus_2 = max_M_sagedus * 0.8
            print("Pulsisagedus peaks olema vahemikus " + str(int(koormus_1))) + " kuni " + str(int(koormus_2))
        if  tuup == 3:
            koormus_1 = max_M_sagedus * 0.8
            koormus_2 = max_M_sagedus * 0.87
            print("Pulsisagedus peaks olema vahemikus " + str(koormus_1) + " kuni " + str(int(koormus_2)))
    else:
        if tuup == 1:
            koormus_1 = max_N_sagedus * 0.5
            koormus_2 = max_N_sagedus * 0.7
            print("Pulsisagedus peaks olema vahemikus " + str(koormus_1) + " kuni " + str(koormus_2))
        if tuup == 2:
            koormus_1 = max_N_sagedus * 0.7
            koormus_2 = max_N_sagedus * 0.8
            print("Pulsisagedus peaks olema vahemikus " + str(koormus_1) + " kuni " + str(koormus_2))
        if tuup == 3:
            koormus_1 = max_N_sagedus * 0.8
            koormus_2 = max_N_sagedus * 0.87
            print("Pulsisagedus peaks olema vahemikus " + str(koormus_1) + " kuni " + str(koormus_2))

koormus()