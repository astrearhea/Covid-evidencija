print("Podaci o corona epidemiji")
print("-------------------------")
corona_gradovi = {"Sarajevo": [10,8,1],"Zenica": [8,5,0], "Tuzla":[31,11,5], "Jajce":[43,8,7]}     #Postojeći gradovi u bazi o corona epidemiji (gradovi u rječniku)
global upit4
global dodano
print("Po gradovima se ispisuje broj zaraženih zatim broj oporavljenih pa broj umrlih.")
def ispis():#ispis stanja u gardovima
    for i in corona_gradovi:
        print("Trenutno stanje za", i,"je:", corona_gradovi[i])                #Ispisuje se trenutno stanje za gradove iz baze/rječnika

ispis()

def upit():
    upit1 = input("Da li želite uraditi ažuriranje stanja po gradovima? ")     #Korisnik se pita da li želi uraditi neko ažuriranje podataka
    if upit1 == "da" or upit1 == "Da" or upit1 == "DA" or upit1 == "dA":       #Mogući odgovori korisnika
        azuriranje()
    else:
        ispis()
        print("Pozdravljamo vas!")                                             #Ukoliko odgovor nije potvrdan, program se završava


def azuriranje():                                                              # Funkcija koja nudi mogućnost ažuriranja podataka
    p= input("Koji grad biste ažurirali? ").capitalize()
    if p in corona_gradovi:
        upit2 = input("Šta biste promjenili? Broj zaraženih, broj oporavljenih ili možda broj umrlih: ")   #Korisnik odabire koji podatak želi promijeniti
        if upit2=="Broj zaraženih" or upit2 == "broj zaraženih" or upit2 == "broj zarazenih" or upit2 == "Broj zarazenih":
            dodano = int(input("Ažurirajte podatke: "))
            corona_gradovi[p][0] = dodano                                      #Vrši se ažuriranje broja zaraženih
            ispis()
            upit()

        elif upit2=="Broj oporavljenih" or upit2 == "broj oporavljenih":
            dodano = int(input("Ažurirajte podatke: "))
            corona_gradovi[p][1] = dodano                                      #Vrši se ažuriranje broja oporavljenih
            ispis()
            upit()

        elif upit2 == "Broj umrlih" or upit2 == "broj umrlih":
            dodano = int(input("Ažurirajte podatke: "))
            corona_gradovi[p][2] = dodano                                      #Vrši se ažuriranje broja umrlih
            ispis()
            upit()

    else:                                                                      #Korisnik ima mogućnost da unese i novi grad, sa novim podacima
        corona_gradovi.update({p: [0, 0, 0]})
        print("Taj grad dosad nije unijet u bazu. Unesite nove podatke sa kojim raspolažete:")
        z = int(input("Broj zaraženih: "))
        o = int(input("Broj oporavljenih: "))
        u = int(input("Broj umrlih: "))
        corona_gradovi[p] = [z,o,u]                                            #Ispisuje se sada trenutno stanje gradova sa novo - unijetim gradom
        ispis()
        upit()


upitm = input("Da li želite uraditi ažuriranje stanja po gradovima? ")
while (upitm.isalpha()==False):                                                # Način na koji se provjerava da li je unos ispravan (da li su unijeta slova)
    upitm = input("Unijeli ste nedozvoljene simbole. Samo slova su mogući unos. Da li želite uraditi ažuriranje stanja po gradovima? ")

if upitm == "da" or upitm == "Da" or upitm == "DA" or upitm == "dA":
  azuriranje()

else:
    ispis()
    print("Pozdravljamo vas!")                                                 #Kraj programa

