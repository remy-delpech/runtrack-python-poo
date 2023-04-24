class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50
    
    def get_marque(self):
        return self._marque
    
    def set_marque(self, nouvelle_marque):
        self._marque = nouvelle_marque
    
    def get_modele(self):
        return self._modele
    
    def set_modele(self, nouveau_modele):
        self._modele = nouveau_modele
    
    def get_annee(self):
        return self._annee
    
    def set_annee(self, nouvelle_annee):
        self._annee = nouvelle_annee
    
    def get_kilometrage(self):
        return self._kilometrage
    
    def set_kilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage
    
    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
    
    def arreter(self):
        self._en_marche = False
    
    def _verifier_plein(self):
        return self._reservoir > 5
    
# création d'une instance de la classe Voiture
ma_voiture = Voiture("Ford", "Fiesta", 2015, 50000)

# test des accesseurs et mutateurs
print(ma_voiture.get_marque())  # Ford
ma_voiture.set_marque("Toyota")
print(ma_voiture.get_marque())  # Toyota

print(ma_voiture.get_modele())  # Fiesta
ma_voiture.set_modele("Corolla")
print(ma_voiture.get_modele())  # Corolla

print(ma_voiture.get_annee())  # 2015
ma_voiture.set_annee(2018)
print(ma_voiture.get_annee())  # 2018

print(ma_voiture.get_kilometrage())  # 50000
ma_voiture.set_kilometrage(60000)
print(ma_voiture.get_kilometrage())  # 60000

# test de la méthode demarrer
ma_voiture.demarrer()  # False, car le réservoir est vide
print(ma_voiture._en_marche)  # False

# test de la méthode arreter
ma_voiture.arreter()
print(ma_voiture._en_marche)  # False

# test de la méthode _verifier_plein (elle ne devrait pas être appelée directement)
print(ma_voiture._verifier_plein())  # False, car le réservoir est vide