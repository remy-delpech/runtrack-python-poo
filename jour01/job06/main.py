class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur :", rectangle.get_longueur()) # Affiche : Longueur : 10
print("Largeur :", rectangle.get_largeur()) # Affiche : Largeur : 5

rectangle.set_longueur(8)
rectangle.set_largeur(3)
print("Nouvelle longueur :", rectangle.get_longueur()) # Affiche : Nouvelle longueur : 8
print("Nouvelle largeur :", rectangle.get_largeur()) # Affiche : Nouvelle largeur : 3