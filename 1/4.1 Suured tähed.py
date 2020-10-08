nimi = input("Sisesta oma ees- ja perenimi: ")

for osa in nimi.split():
    print(osa.capitalize(), end=" ")