class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print("Marque = {}".format(self.marque))
        print("Modèle = {}".format(self.modele))
        print("Année = {}".format(self.annee))
        print("Prix = {}".format(self.prix))

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes = {}".format(self.portes))

    def demarrer(self):
        print("Je démarre ma voiture {} {}.".format(self.marque, self.modele))


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues = {}".format(self.roues))

    def demarrer(self):
        print("Je démarre ma moto {} {}.".format(self.marque, self.modele))

# Instanciation de l'objet Voiture et appel de la méthode informationsVehicule
ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

# Instanciation de l'objet Moto et appel de la méthode informationsVehicule
ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
ma_moto.informationsVehicule()
ma_moto.demarrer()