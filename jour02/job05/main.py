import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * self.radius**2
        
# Création d'un objet Rectangle
rectangle = Rectangle(5, 10)
# Appel de la méthode aire de la classe Rectangle
print(rectangle.aire())  # affiche 50

# Création d'un objet Cercle
cercle = Cercle(5)
# Appel de la méthode aire de la classe Cercle
print(cercle.aire())  # affiche environ 78.54