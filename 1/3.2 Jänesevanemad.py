ringid = int(input("Siseestage ringide arv: "))

ring = 1

porgandite_arv = 0

while(ring <= ringid):
    print(str(ring) + ".ring")
    #kas hetkel on paarisarvuline ring?
    if(ring % 2 == 0):#siin antakse porgandeid, nii palju kui on ringi number
        print("said" + " " + str(ring) + " " + "porgandeid")
        porgandite_arv = porgandite_arv + ring
        print("Hetkel on kokku" + " " + str(porgandite_arv) + " " + "porgandit")

    ring += 1



