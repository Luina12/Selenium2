#klasa to szablon
class Czlowiek():
    def __init__(self,imie):
        print('Wywoluje konstruktor')
        self.imie=imie
    #cialo klasy
        gatunek='human'
        def podskocz(self):
            print('podskoczylem')
        def __del__(self):
            print ('Do widzenia,babcia Gienia')
        class Dziecko(Czlowiek):
            def bawimy_sie(self):
                print('juhuuu')

#Teraz tworzymy obiekty(instancje klasy)
marcin=Czlowiek("marcin")
#odwolanie do metody
marcin.podskocz()
#odwolanie do atrybutu
print(marcin.gatunek)
basia=Czlowiek()
basia=Czlowiek('Basia')
print(basia.imie)
barcin=Dziecko('barcin')
barcin.bawimy_sie()
