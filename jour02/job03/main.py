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
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
# Instanciation de la classe Rectangle
r = Rectangle(5, 10)

# Affichage de la longueur et de la largeur
print("Longueur :", r.get_longueur())
print("Largeur :", r.get_largeur())

# Modification de la longueur et de la largeur
r.set_longueur(8)
r.set_largeur(6)

# Affichage du périmètre et de la surface
print("Périmètre :", r.perimetre())
print("Surface :", r.surface())

# Instanciation de la classe Parallelepipede
p = Parallelepipede(3, 4, 5)

# Affichage de la longueur, de la largeur et de la hauteur
print("Longueur :", p.get_longueur())
print("Largeur :", p.get_largeur())
print("Hauteur :", p.get_hauteur())

# Modification de la longueur, de la largeur et de la hauteur
p.set_longueur(6)
p.set_largeur(8)
p.set_hauteur(10)

# Affichage du périmètre, de la surface et du volume
print("Périmètre :", p.perimetre())
print("Surface :", p.surface())
print("Volume :", p.volume())