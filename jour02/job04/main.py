class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur
        
# Création d'un objet Rectangle
rectangle = Rectangle(5, 10)

# Appel de la méthode aire de la classe Rectangle
print(rectangle.aire())  # affiche 50