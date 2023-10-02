import random
import time


# Klass för att rita spelbrädan
class Bräde:
    @staticmethod  # Statisk metod, metod utan self.
    def rita_bräde(bräde):
        storlek = len(bräde)  # Hämta storleken på brädan
        print("   " + "   ".join(map(str, range(storlek))))  # Skriver ut kolumnnummer ovanför brädan

        for rad_num, rad in enumerate(bräde):
            print(rad_num, " | ".join(rad))  # Rita ut varje rad i brädan med separerade kolumner

            if rad_num < storlek - 1:  # Om det inte är den sista raden, rita en rad med streck under varje rad för att markera gränserna
                print("  ", "-" * (4 * storlek - 1))


# Klass för att kolla om en spelare har vunnit
class Vinst:
    @staticmethod  # Statisk metod, metod utan self.
    def kolla_vinst(bräde, spelare):
        storlek = len(bräde)  # Hämta storleken på brädan

        # Kolla rader och kolumner
        for i in range(storlek):
            # Kolla om alla element i raden "i" har samma värde som spelare
            if all(bräde[i][j] == spelare for j in range(storlek)) or all(
                    bräde[j][i] == spelare for j in range(storlek)):
                return True  # Returnera True om någon rad eller kolumn har alla element med spelarens värde

        # Kolla diagonalerna
        if all(bräde[i][i] == spelare for i in range(storlek)) or all(
                bräde[i][storlek - 1 - i] == spelare for i in range(storlek)):
            return True  # Returnera True om någon av de två diagonalerna har alla element med spelarens värde

        return False  # Om ingen vinst hittades, returnera False


# Klass för datorns drag
class DatornsDrag:
    @staticmethod  # Statisk metod, metod utan self.
    def datorns_drag(bräde):
        storlek = len(bräde)  # Hämta storleken på brädan.
        while True:
            rad = random.randint(0, storlek - 1)  # Slumpmässigt välj en rad inom brädans gränser
            kolumn = random.randint(0, storlek - 1)  # Slumpmässigt välj en kolumn inom brädans gränser

            if bräde[rad][kolumn] == " ":  # Om den valda positionen är tom
                return rad, kolumn  # Returnera rad och kolumn för datorns drag


class Spela:
    def __init__(self, storlek):
        self.storlek = storlek  # Spara brädans storlek som en instansvariabel

    # Funktion för att spela mot datorn
    def spela_mot_datorn(self):
        brädet = [[" " for _ in range(self.storlek)] for _ in range(self.storlek)]  # Skapar ett tomt spelbräda
        bräde_instans = Bräde()  # Skapar instans av klassen-bräde för att rita brädan
        aktuell_spelare = "X"  # Spelaren som börjar
        antal_drag = 0  # Variabel som har koll på antalet drag

        while True:
            bräde_instans.rita_bräde(brädet)  # Rita spelbrädan
            try:
                if aktuell_spelare == "X":  # Om det är spelarens tur
                    print(f"Spelare {aktuell_spelare}, ange rad (0-{self.storlek - 1}) och kolumn (0-{self.storlek - 1}) för ditt drag (t.ex. 1 1): ")
                    rad, kolumn = map(int, input().split())

                    # Ta reda på om spelarens drag är giltigt
                    if rad < 0 or rad >= self.storlek or kolumn < 0 or kolumn >= self.storlek or brädet[rad][kolumn] != " ":
                        print("Ogiltigt drag. Försök igen.")
                        time.sleep(1)
                        continue
                else:
                    print(f"Datorns tur...")
                    time.sleep(1)  # Väntar en sekund så att man ser vad som händer
                    datorns_drag_instans = DatornsDrag()  # Skapar en instans av klassen-DatornsDrag
                    rad, kolumn = datorns_drag_instans.datorns_drag(brädet)  # Använd Klassen-DatornsDrag för att bestämma datorns drag

                brädet[rad][kolumn] = aktuell_spelare  # Utför draget
                antal_drag += 1  # Ökar variabeln antal_drag med + 1.

                vinst_instans = Vinst()  # Skapar en instans av Klassen-Vinst för att kontrollera om någon har vunnit
                if vinst_instans.kolla_vinst(brädet, aktuell_spelare):  # Kontrollera om någon har vunnit
                    bräde_instans.rita_bräde(brädet)  # Rita brädan igen för att visa vinsten
                    if aktuell_spelare == "X":
                        print(f"Spelare {aktuell_spelare} har vunnit!")
                        time.sleep(1)
                    else:
                        print("Datorn har vunnit!")
                        time.sleep(1)
                    break
                elif antal_drag == self.storlek * self.storlek:  # Har antalet drag som går att göra dragits och ingen har vunnit är det oavgjort
                    bräde_instans.rita_bräde(brädet)
                    print("Det blev oavgjort!")
                    time.sleep(1)
                    break

                aktuell_spelare = "O" if aktuell_spelare == "X" else "X"  # Byt spelare

            except ValueError:  # Felhantering för ogiltig inmatning
                print("Felaktig inmatning. Ange ett giltigt drag (ex. 0 2)")
                time.sleep(1)
                continue

    # Funktion för att spela mot en annan spelare
    def spela_mot_spelare(self, bräde_instans):
        brädet = [[" " for _ in range(self.storlek)] for _ in range(self.storlek)]  # Skapar en tom spelbräda
        aktuell_spelare = "X"  # Spelaren som börjar
        antal_drag = 0  # Räknar antal drag

        while True:
            bräde_instans.rita_bräde(brädet)  # Rita spelbrädan
            try:
                print(f"Spelare {aktuell_spelare}, ange rad (0-{self.storlek - 1}) och kolumn (0-{self.storlek - 1}) för ditt drag (t.ex. 1 1): ")
                rad, kolumn = map(int, input().split())

                # Validera om spelarens drag är giltigt
                if rad < 0 or rad >= self.storlek or kolumn < 0 or kolumn >= self.storlek or brädet[rad][kolumn] != " ":
                    print("Ogiltigt drag. Försök igen.")
                    time.sleep(1)
                    continue

                brädet[rad][kolumn] = aktuell_spelare  # Utför draget
                antal_drag += 1  # Öka antalet drag med 1

                vinst_instans = Vinst()  # Skapar en instans av Vinst-klassen för att kontrollera om någon har vunnit
                if vinst_instans.kolla_vinst(brädet, aktuell_spelare):  # Kontrollera om någon har vunnit
                    bräde_instans.rita_bräde(brädet)  # Rita brädan igen för att visa vinsten
                    print(f"Spelare {aktuell_spelare} har vunnit!")
                    time.sleep(1)
                    break
                elif antal_drag == self.storlek * self.storlek:  # Vid antalet drag som får plats i brädan utan vinnare är det oavgjort
                    bräde_instans.rita_bräde(brädet)  # Rita brädan igen för att visa den slutliga ställningen
                    print("Det blev oavgjort!")
                    time.sleep(1)  # Väntar 1 sekund med att gå vidare så att spelaren hinner läsa meddelandet
                    break

                aktuell_spelare = "O" if aktuell_spelare == "X" else "X"  # Byt aktuell spelare inför nästa drag

            except ValueError:  # Felhantering vid ogiltig inmatning
                print("Felaktig inmatning. Ange ett giltigt drag (ex. 0 2)")
                time.sleep(1)  # Vänta en sekund med att visa meddelandet
                continue


# Huvudmenyn
def huvudmeny():
    bräde_instans = Bräde()  # Rita brädet
    while True:
        print("Välj läge:")
        print("1. Spela mot datorn")
        print("2. Spela mot en annan spelare")
        print("3. Avsluta")
        val = input("Ange ditt val (1/2/3): ")
        play = Spela(3) # Värdet i parentesen anger exempelvis om det blir 3 eller 4 i rad.
        if val == "1":
            play.spela_mot_datorn()
        elif val == "2":
            play.spela_mot_spelare(bräde_instans)
        elif val == "3":
            break  # Avsluta programmet
        else:
            print("Ogiltigt val. Försök igen.")
            time.sleep(1)  # Väntar en sekund så att spelaren hinner läsa felmeddelandet


# Kör huvudmenyn när programmet körs
huvudmeny()
