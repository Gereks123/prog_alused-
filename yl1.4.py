nimi = str(input('Sisestage oma nimi:'))
lubatud_kiirus = int(input('Sisestage lubatud kiirus (km/h): '))
tegelik_kiirus = int(input('Sisestage tegelik kiirus (km/h): '))
trahvitav_kiirus = tegelik_kiirus - lubatud_kiirus
trahv = min(190, trahvitav_kiirus * 3)
print(trahv)
